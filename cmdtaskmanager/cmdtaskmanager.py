import argparse
from .config.consts import DB_LOCATION
from .config.core import setup_config
from .database.db_manager import DBManager
from .task.subparsers import register_task_subparsers
from .tag.entities import *
from .project.entities import *
from .task.entities import *
from .task.core import setup_base_statuses


def main():
    setup_config()
    db_manager = DBManager(DB_LOCATION)
    setup_base_statuses(db_manager.engine)
    
    parser = argparse.ArgumentParser(description='Your daily task manager.')
    subparsers = parser.add_subparsers()
    register_task_subparsers(subparsers)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
