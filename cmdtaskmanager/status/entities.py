from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from ..shared.display import GREY
from ..database.base import Base
from ..shared.core import entity_to_repr


class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    color = Column(String, nullable=False, default=GREY)
    date_created = Column(DateTime, nullable=False, default=datetime.utcnow)
 
    def __repr__(self):
        return entity_to_repr(self, 'Status',
            ['id', 'name', 'description', 'color', 'date_created'])

