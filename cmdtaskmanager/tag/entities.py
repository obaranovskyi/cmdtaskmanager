from datetime import datetime
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from sqlalchemy.orm import relationship
from ..shared.core import entity_to_repr
from ..database.base import Base

task_tag_table = Table(
    "task_tag",
    Base.metadata,
    Column("task_id", ForeignKey("task.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)

class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    date_created = Column(DateTime, nullable=False, default=datetime.utcnow)
    task = relationship('Task', secondary=task_tag_table, back_populates='tags')
    
    def __repr__(self):
        return entity_to_repr(self, 'Tag',
            ['id', 'name', 'description', 'date_created'])
