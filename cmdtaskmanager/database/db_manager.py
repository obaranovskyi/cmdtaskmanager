from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..config.consts import DB_LOCATION
from .base import Base


class DBManager:

    def __init__(self, database_name):
        self.database_name = database_name
        self.setup()

    def setup(self):
        self.create_engine()
        self.create_tables()
        self.create_session()

    def create_engine(self):
        self.engine = create_engine(
            f"sqlite:///{self.database_name}")

    def create_tables(self):
        Base.metadata.create_all(
            self.engine, checkfirst=True)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def end_session(self):
        session.commit()
        session.close()

db = DBManager(DB_LOCATION)
session = db.session
        
