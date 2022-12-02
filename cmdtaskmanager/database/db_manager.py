from sqlalchemy import create_engine
from .base import Base


class DBManager:

    def __init__(self, database_name):
        self.database_name = database_name
        self.setup()

    def setup(self):
        self.create_engine()
        self.create_tables()

    def create_engine(self):
        self.engine = create_engine(
            f"sqlite:///{self.database_name}")

    def create_tables(self):
        Base.metadata.create_all(
            self.engine, checkfirst=True)

