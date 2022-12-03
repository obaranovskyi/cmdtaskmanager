from sqlalchemy.orm import sessionmaker
from .consts import STATUSES
from .entities import Status


def setup_base_statuses(engine):
    Session = sessionmaker(bind=engine)
    with Session.begin() as session:
        res = session.query(Status).filter(
            Status.name.in_(STATUSES)).all()
        if not len(res):
            for sv in STATUSES:
                session.add(Status(name=sv))
