import sqlalchemy as database

from .tables import get_tables


class DBManager:
    def __init__(self, database_name):
        self.metadata = database.MetaData()
        self.database_name = database_name

    def setup(self):
        self.create_engine()
        self.connect_to_db()
        self.tables = self.create_tables()

    def create_engine(self):
        self.engine = database.create_engine(
            f"sqlite:///{self.database_name}")

    def connect_to_db(self):
        self.connection = self.engine.connect()

    def create_tables(self):
        tables = get_tables(self.metadata, self.engine)
        self.metadata.create_all(self.engine)
        return tables

