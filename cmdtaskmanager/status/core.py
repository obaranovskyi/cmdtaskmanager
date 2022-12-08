from sqlalchemy.sql.expression import asc
from .consts import NOT_STARTED, STATUSES
from .entities import Status
from ..database.db_manager import session


def setup_base_statuses():
    status_names = [s.name for s in STATUSES]
    res = session.query(Status).filter(
        Status.name.in_(status_names)).all()
    if not len(res):
        for s in STATUSES:
            session.add(Status(name=s.name, description=s.description))

def get_status_by_name(name):
    return session.query(Status) \
        .filter(Status.name==name).one_or_none()

def get_not_started():
    return get_status_by_name(NOT_STARTED.name)

def get_statuses_to_display(limit):
    return session.query(Status).order_by(asc(Status.id)).limit(limit).all()
