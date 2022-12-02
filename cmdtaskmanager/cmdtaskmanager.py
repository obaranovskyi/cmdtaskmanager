#!/bin/python3
import argparse
from .config.consts import DB_LOCATION
from .config.core import setup_config
from .database.db_manager import DBManager
from .task.subparsers import register_task_subparsers

def main():
    setup_config()
    db_manager = DBManager(DB_LOCATION)
    db_manager.setup()

    parser = argparse.ArgumentParser(description='Your daily task manager.')
    subparsers = parser.add_subparsers()
    register_task_subparsers(subparsers)
    args = parser.parse_args()
    print(args)
    


if __name__ == '__main__':
    main()
