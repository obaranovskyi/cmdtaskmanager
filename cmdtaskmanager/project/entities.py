from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from ..shared.core import entity_to_repr
from ..database.base import Base


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    finish_date = Column(DateTime)
 
    def __repr__(self):
        return entity_to_repr(self, 'Project',
            ['id', 'name', 'description', 'finish_date'])

