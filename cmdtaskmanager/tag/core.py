from .errors import TagNameAlreadyExists
from .entities import Tag
from ..database.db_manager import session


def create_tag(name):
    exists = session.query(Tag.name==name).one_or_none()
    if exists:
        raise TagNameAlreadyExists()
    tag = Tag(name=name)
    session.add(tag)
