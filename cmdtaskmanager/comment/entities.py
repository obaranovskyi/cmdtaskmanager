from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from ..database.base import Base
from ..shared.core import entity_to_repr


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    task_id = Column(Integer, ForeignKey('task.id'))
    task = relationship('Task')
    date_created = Column(DateTime, nullable=False, default=datetime.utcnow)
 
    def __repr__(self):
        return entity_to_repr(self, 'Comment',
            ['id', 'content', 'date_created'])

