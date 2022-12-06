from .consts import NOT_STARTED, STATUSES
from .entities import Status
from ..database.db_manager import session


def setup_base_statuses():
    res = session.query(Status).filter(
        Status.name.in_(STATUSES)).all()
    if not len(res):
        for sv in STATUSES:
            session.add(Status(name=sv))

def get_status_by_name(name):
    return session.query(Status) \
        .filter(Status.name==name).one_or_none()

def get_not_started():
    return get_status_by_name(NOT_STARTED)