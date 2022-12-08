from .errors import InvalidStatusIdError, InvalidStatusNameError
from .consts import NOT_STARTED, STATUSES
from .entities import Status
from ..database.db_manager import session


def setup_base_statuses():
    status_names = [s.name for s in STATUSES]
    res = session.query(Status).filter(
        Status.name.in_(status_names)).all()
    if not len(res):
        for s in STATUSES:
            status = Status(
                name=s.name,
                description=s.description,
                color=s.color
            )
            session.add(status)

def get_status_by_name(name):
    """
    Raises:
        - `InvalidStatusNameError` -- When a status with such a name doesn't exist.
    """
    status = session.query(Status) \
        .filter(Status.name==name).one_or_none()
    if not status:
        raise InvalidStatusNameError()
    return status

def get_not_started():
    return get_status_by_name(NOT_STARTED.name)

def get_statuses_to_display(limit):
    return session.query(Status).order_by(asc(Status.id)).limit(limit).all()

def get_status_by_id(status_id):
    """
    Raises:
        - `InvalidStatusIdError` -- When the status with the given id doesn't exist.
    """
    status = session.query(Status).filter(Status.id==status_id).one_or_none();
    if not status:
        raise InvalidStatusIdError()
    return status

def get_status_by_name_or_id(status_name, status_id):
    """
    Raises:
        - `InvalidStatusIdError` -- When the status with the given id doesn't exist.
        - `InvalidStatusNameError` -- When a status with such a name doesn't exist.
    """
    if status_id:
        return get_status_by_id(status_id)
    return get_status_by_name(status_name)
