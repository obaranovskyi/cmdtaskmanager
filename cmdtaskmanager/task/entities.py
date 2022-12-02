from sqlalchemy import (
    CheckConstraint, Column, ForeignKey,
    String, Table, Text, Integer)
from sqlalchemy.orm import relationship

from cmdtaskmanager.shared.core import entity_to_repr
from ..database.base import Base


task_tag_table = Table(
    "task_tag",
    Base.metadata,
    Column("task_id", ForeignKey("tag.id"), primary_key=True),
    Column("tag_id", ForeignKey("task.id"), primary_key=True),
)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    long_description = Column(Text)
    priority = Column(Integer, CheckConstraint('priority > -1 AND priority < 11'))
    status_id = Column(Integer, ForeignKey('status.id'))
    status = relationship('Status')
    tags = relationship('Tag', secondary=task_tag_table, back_populates='task')

    def __repr__(self):
        return entity_to_repr(self, 'Task',
            ['id', 'title', 'description', 'long_description', 'priority', 'status'])


class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True)
    value = Column(String, unique=True)
 
    def __repr__(self):
        return entity_to_repr(self, 'Status', ['id', 'value'])


class Tag(Base):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True)
    value = Column(String, unique=True)
    task = relationship('Task', secondary=task_tag_table, back_populates='tags')
    
    def __repr__(self):
        return entity_to_repr(self, 'Tag', ['id', 'value'])
    
