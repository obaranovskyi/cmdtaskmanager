from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from ..shared.core import entity_to_repr
from ..database.base import Base


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    status_id = Column(Integer, ForeignKey('status.id'), nullable=False)
    status = relationship('Status')
    date_created = Column(DateTime, nullable=False, default=datetime.utcnow)
    finish_date = Column(DateTime)
 
    def __repr__(self):
        return entity_to_repr(self, 'Project',
            ['id', 'name', 'description', 'date_created', 'finish_date'])

