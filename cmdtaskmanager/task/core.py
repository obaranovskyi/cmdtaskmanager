from datetime import datetime
from sqlalchemy.sql.expression import desc, or_

from cmdtaskmanager.status.consts import NOT_STARTED, REMOVED
from ..tag.core import get_tags_by_names_or_ids
from ..shared.file_core import get_file_content
from ..status.core import get_not_started, get_status_by_name_or_id, get_status_by_name
from ..project.core import get_project_by_name_or_id
from ..database.db_manager import session
from .entities import Task
from .errors import InvalidTaskFinishDateError, InvalidTaskIdError


def create_task(title, priority, description,
                long_description, finish_date, project_id,
                project_name, tag_names, tag_ids):
    """
    Raises:
        - `InvalidTaskFinishDateError` -- When the task finish date isn't later than now.
        - `NoSuchFileError` -- When a file that was given to set a `long_description` doesn't exist.
        - `IsNotFileError` -- When a file that was given to set a `long_description` isn't readable.
        - `InvalidProjectIdError` -- When the project with the given id doesn't exist.
        - `InvalidProjectNameError` -- When the project with the given name doesn't exist.
        - `InvalidTagIdError` -- When the tag with the given id doesn't exist.
    """
    if finish_date and finish_date < datetime.now():
        raise InvalidTaskFinishDateError()
    long_description_content = get_long_description_content(long_description)
    project = get_project_by_name_or_id(project_id, project_name)
    tags = get_tags_by_names_or_ids(tag_names, tag_ids)
    task = Task(
        title=title,
        priority=priority,
        description=description,
        long_description=long_description_content,
        finish_date=finish_date,
        status=get_not_started(),
        project=project,
        tags=tags
    )
    session.add(task)

def update_task(task_id, title, priority, description,
                status_id, status_name, long_description,
                finish_date, project_id, project_name,
                tag_names, tag_ids):
    """
    Raises:
        - `InvalidTaskIdError` - When the task with a given id doesn't exist.
        - `InvalidTaskFinishDateError` -- When the task finish date isn't later than now.
        - `NoSuchFileError` -- When a file that was given to set a `long_description` doesn't exist.
        - `IsNotFileError` -- When a file that was given to set a `long_description` isn't readable.
        - `InvalidProjectIdError` -- When the project with the given id doesn't exist.
        - `InvalidProjectNameError` -- When the project with the given name doesn't exist.
        - `InvalidTagIdError` -- When the tag with the given id doesn't exist.
        - `InvalidStatusIdError` -- When the status with the given id doesn't exist.
        - `InvalidStatusNameError` -- When a status with such a name doesn't exist.
    """
    task_to_update = get_task_by_id(task_id)
    if finish_date and finish_date < datetime.now():
        raise InvalidTaskFinishDateError()
    task_to_update.finish_date = finish_date if finish_date else task_to_update.finish_date
    task_to_update.title = title if title else task_to_update.title
    task_to_update.priority = priority if priority else task_to_update.priority
    task_to_update.description = description if description else task_to_update.description
    if status_name or status_id:
        task_to_update.status = get_status_by_name_or_id(status_name, status_id)
        start_project_if_needed(task_to_update)
    if long_description:
        task_to_update.long_description = get_long_description_content(long_description)
    if project_id or project_name:
        task_to_update.project = get_project_by_name_or_id(project_id, project_name)
    if tag_names or tag_ids:
        task_to_update.tags = get_tags_by_names_or_ids(tag_names, tag_ids)
    session.commit()


def remove_task(task_id):
    """
        Raises:
            - `InvalidTaskIdError` - When the task with a given id doesn't exist.
    """
    task = get_task_by_id(task_id)
    session.delete(task)
    session.commit()


def update_task_status(task_id, status_name):
    """
    Raises:
        - `InvalidTaskIdError` - When the task with a given id doesn't exist.
        - `InvalidStatusNameError` -- When a status with such a name doesn't exist.
    """
    task_to_update = get_task_by_id(task_id)
    task_to_update.status = get_status_by_name(status_name)
    session.commit()
    start_project_if_needed(task_to_update)

def get_task_by_id(task_id):
    """
        Raises:
            - `InvalidTaskIdError` - When the task with a given id doesn't exist.
    """
    task = session.query(Task).filter(Task.id==task_id).one_or_none()
    if not task:
        raise InvalidTaskIdError()
    return task


def get_long_description_content(long_description):
    """
    Raises:
        - `NoSuchFileError` -- When a file that was given to set a `long_description` doesn't exist.
        - `IsNotFileError` -- When a file that was given to set a `long_description` isn't readable.
    """
    return get_file_content(long_description) \
        if long_description \
        else None

def get_tasks_to_display(limit, title, description, project_name,
                         project_id, tag_names, tag_ids):
    query = session.query(Task)
    if project_id or project_name:
        query = query.filter(
            or_(Task.project_id==project_id,
                Task.project.has(name=project_name))
        )
    if title:
        query = query.filter(Task.title.ilike(f'%{title}%'))
    if description:
        query = query.filter(Task.description.ilike(f'%{description}%'))
    if tag_ids:
        from ..tag.entities import task_tag
        query = query.join(task_tag,
            (Task.id == task_tag.c.task_id) & (task_tag.c.tag_id.in_(tag_ids)))
    if tag_names:
        from ..tag.entities import task_tag, Tag
        query = query.join(task_tag).join(Tag,
            (Tag.id == task_tag.c.tag_id) & (Tag.name.in_(tag_names)))
    return query                            \
        .order_by(desc(Task.date_created))  \
        .limit(limit)                       \
        .all()

def get_tasks_by_project_id(project_id):
    return session.query(Task).filter(Task.project.has(id=project_id)).all()

def get_tasks_by_tag_id(tag_id):
    from ..tag.entities import task_tag, Tag
    query_task_tag = session.query(Task).join(task_tag).join(Tag)
    tasks = query_task_tag.filter(task_tag.c.tag_id==tag_id)
    return tasks.all()

def start_project_if_needed(task):
    if task.status.name not in [NOT_STARTED.name, REMOVED.name] and \
      (task.project and task.project.status.name == NOT_STARTED.name):
        from ..project.core import start_project_by_id
        start_project_by_id(task.project.id)
