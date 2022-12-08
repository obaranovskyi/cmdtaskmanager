from datetime import datetime

from sqlalchemy import desc
from ..tag.core import get_tags_by_names_or_ids
from ..shared.file_core import get_file_content
from ..status.core import get_not_started
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

def get_tasks_to_display(limit):
    return session.query(Task).order_by(desc(Task.date_created)).limit(limit).all()
