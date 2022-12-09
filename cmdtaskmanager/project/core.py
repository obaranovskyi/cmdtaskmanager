from datetime import datetime

from sqlalchemy.sql.expression import and_, desc
from .errors import *
from ..status.core import get_not_started, get_status_by_name_or_id
from .entities import Project
from ..database.db_manager import session


def create_project(name, description, finish_date):
    """
    Raises:
        - `InvalidProjectFinishDateError` -- When the project finish date isn't later than now.
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

def update_project(project_id, name, description, finish_date, status_id, status_name,):
    """
    Raises:
        - `InvalidProjectIdError` -- When the project with the given id doesn't exist.
        - `InvalidProjectFinishDateError` -- When the project finish date isn't later than now.
        - `ProjectNameAlreadyExists` -- When a project with such a name already exists.
        - `InvalidStatusIdError` -- When the status with the given id doesn't exist.
        - `InvalidStatusNameError` -- When a status with such a name doesn't exist.
    """
    project_to_update = session.query(Project).filter(Project.id==project_id).one_or_none()
    if not project_to_update:
        raise InvalidProjectIdError()
    if finish_date and finish_date < datetime.now():
        raise InvalidProjectFinishDateError()
    if name:
        exists = session.query(Project).filter(
            and_(Project.name==name, Project.id!=project_id)).one_or_none()
        if exists:
            raise ProjectNameAlreadyExists()
    project_to_update.name = name or project_to_update.name
    project_to_update.description = description or project_to_update.description
    project_to_update.finish_date = finish_date or project_to_update.finish_date
    if status_name or status_id:
        project_to_update.status = get_status_by_name_or_id(status_name, status_id)
    session.commit()

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

def get_projects_to_display(limit):
    return session.query(Project).order_by(desc(Project.date_created)).limit(limit).all()
