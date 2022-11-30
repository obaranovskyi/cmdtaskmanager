#!/bin/python3
from .config.consts import DB_LOCATION
from .config.core import setup_config
from .database.db_manager import DBManager

def main():
    setup_config()
    db_manager = DBManager(DB_LOCATION)
    db_manager.setup()

if __name__ == '__main__':
    main()
