from datetime import datetime
from .errors import *
from ..status.core import get_not_started
from .entities import Project
from ..database.db_manager import session


def create_project(name, description, finish_date):
    """
    Raises:
        - `InvalidProjectIdError` -- When the project with the given id doesn't exist.
        - `ProjectNameAlreadyExists` -- When a project with such a name already exists.
    """
    if finish_date < datetime.now():
        raise InvalidProjectFinishDateError()
    exists = session.query(Project).filter(Project.name==name).one_or_none()
    if exists:
        raise ProjectNameAlreadyExists()
    project = Project(
        name=name,
        description=description,
        status=get_not_started(),
        finish_date=finish_date
    )
    session.add(project)

def get_project_by_name(name):
    """
    Raises:
        - `InvalidProjectNameError` -- When a project with such a name doesn't exist.
    """
    project = session.query(Project).filter(Project.name==name).one_or_none()
    if not project: 
        raise InvalidProjectNameError()
    return project

def get_project_by_id(id):
    """
    Raises:
        - `InvalidProjectIdError` -- When the project with the given id doesn't exist.
    """
    project = session.query(Project).filter(Project.id==id).one_or_none()
    if not project: 
        raise InvalidProjectIdError()
    return project

def get_project_by_name_or_id(project_id, project_name):
    """
    Raises:
        - `InvalidProjectIdError` -- When the project with the given id doesn't exist.
        - `InvalidProjectNameError` -- When the project with the given name doesn't exist.
    """
    if not project_id and not project_name:
        return None
    if project_id:
        return get_project_by_id(project_id)
    return get_project_by_name(project_name)
