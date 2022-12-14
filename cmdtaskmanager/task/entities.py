from datetime import datetime
from sqlalchemy.sql.schema import CheckConstraint, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from ..shared.core import entity_to_repr
from ..database.base import Base
from ..tag.entities import task_tag


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False) # consider doing it uniq in scope of project
    description = Column(String)
    long_description = Column(Text)
    priority = Column(Integer, CheckConstraint('priority > -1 AND priority < 11'), nullable=False)
    status_id = Column(Integer, ForeignKey('status.id'), nullable=False)
    status = relationship('Status')
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship('Project')
    tags = relationship('Tag', secondary=task_tag, back_populates='task')
    date_created = Column(DateTime, nullable=False, default=datetime.utcnow)
    finish_date = Column(DateTime)

    def __repr__(self):
        return entity_to_repr(self, 'Task',
            ['id', 'title', 'description', 'long_description',
             'priority', 'status', 'tags', 'date_created', 'finish_date'])


