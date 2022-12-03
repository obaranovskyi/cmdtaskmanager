from .consts import STATUSES
from .entities import Status
from ..database.db_manager import session


def setup_base_statuses():
    res = session.query(Status).filter(
        Status.name.in_(STATUSES)).all()
    if not len(res):
        for sv in STATUSES:
            session.add(Status(name=sv))
