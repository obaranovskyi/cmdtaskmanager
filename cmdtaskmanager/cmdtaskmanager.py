import argparse
from sqlalchemy.orm import sessionmaker

from .config.consts import DB_LOCATION
from .config.core import setup_config
from .database.db_manager import DBManager
from .task.subparsers import register_task_subparsers
from .task.entities import *
from .task.consts import STATUSES, NOT_STARTED

def main():
    setup_config()
    db_manager = DBManager(DB_LOCATION)

    Session = sessionmaker(bind=db_manager.engine)

    # TODO: This has to be extracted from here
    # INFO: Create base statuses
    with Session.begin() as session:
        res = session.query(Status).filter(
            Status.value.in_(STATUSES)).all()
        if not len(res):
            for sv in STATUSES:
                session.add(Status(value=sv))

        tasks = session.query(Task).all()
        print(tasks)

        # Adding tags
        # session.add(Tag(value='TestProject'))
        # session.add(Tag(value='RealProject'))
        
        # Adding task
        # tags = session.query(Tag).all()
        # not_started_status = session.query(Status).filter(Status.value==NOT_STARTED).one()
        # session.add(
        #     Task(title='Title', description='Description',
        #          long_description='Long description', priority=5,
        #          status=not_started_status, tags=tags))

        # INFO: Important to note that in with scope we're closing the session
    
    # parser = argparse.ArgumentParser(description='Your daily task manager.')
    # subparsers = parser.add_subparsers()
    # register_task_subparsers(subparsers)
    # args = parser.parse_args()
    # print(args)


if __name__ == '__main__':
    main()
