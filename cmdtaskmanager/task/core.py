from datetime import datetime
from ..shared.file_core import get_file_content
from ..status.core import get_not_started
from ..project.core import get_project_by_name_or_id
from ..database.db_manager import session
from .entities import Task
from .errors import InvalidTaskFinishDateError


def create_task(title, priority, description,
                long_description, finish_date, project_id,
                project_name):
    """
    Raises:
        - `InvalidTaskFinishDateError` -- When the task finish date isn't later than now.
        - `NoSuchFileError` -- When a file that was given to set a `long_description` doesn't exist.
        - `IsNotFileError` -- When a file that was given to set a `long_description` isn't readable.
        - `InvalidProjectIdError` -- When the project with the given id doesn't exist.
        - `InvalidProjectNameError` -- When the project with the given name doesn't exist.
    """
    if finish_date < datetime.now():
        raise InvalidTaskFinishDateError()
    long_description_content = get_long_description_content(long_description)
    project = get_project_by_name_or_id(project_id, project_name)
    task = Task(
        title=title,
        priority=priority,
        description=description,
        long_description=long_description_content,
        finish_date=finish_date,
        status=get_not_started(),
        project=project
    )
    session.add(task)

def get_long_description_content(long_description):
    """
    Raises:
        - `NoSuchFileError` -- When a file that was given to set a `long_description` doesn't exist.
        - `IsNotFileError` -- When a file that was given to set a `long_description` isn't readable.
    """
    return get_file_content(long_description) \
        if long_description \
        else None

