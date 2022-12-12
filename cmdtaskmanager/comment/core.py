from sqlalchemy.sql.expression import desc
from .errors import InvalidCommentIdError
from .entities import Comment
from ..task.core import get_task_by_id
from ..database.db_manager import session


def create_comment(task_id, content):
    """
        Raises:
            - `InvalidTaskIdError` - When the task with a given id doesn't exist.
    """
    task = get_task_by_id(task_id)
    comment = Comment(content=content, task=task)
    session.add(comment)
    session.commit()

def update_comment(comment_id, task_id, content):
    """
        Raises:
            - `InvalidCommentIdError` - When the comment with a given id doesn't exist.
            - `InvalidTaskIdError` - When the task with a given id doesn't exist.
    """
    comment = get_comment_by_id(comment_id)
    comment.task = get_task_by_id(task_id) if task_id else comment.task
    comment.content = content if content else comment.content
    session.commit()

def remove_comment(comment_id):
    """
        Raises:
            - `InvalidCommentIdError` - When the comment with a given id doesn't exist.
    """
    comment = get_comment_by_id(comment_id)
    session.delete(comment)
    session.commit()

def get_comment_by_id(comment_id):
    comment = session.query(Comment).filter(Comment.id==comment_id).one_or_none()
    if not comment:
        raise InvalidCommentIdError()
    return comment

def get_comments_by_task_id(task_id):
    return session.query(Comment)               \
        .order_by(desc(Comment.date_created))   \
        .filter(Comment.task_id==task_id).all()
