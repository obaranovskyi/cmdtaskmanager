from .errors import TagNameAlreadyExists, InvalidTagIdError
from .entities import Tag
from ..database.db_manager import session


def create_tag(name):
    """
    Raises:
        - `TagNameAlreadyExists` -- When a tag with such a name already exists.
    """
    exists = session.query(Tag.name==name).one_or_none()
    if exists:
        raise TagNameAlreadyExists()
    tag = Tag(name=name)
    session.add(tag)

def get_or_create_tag(tag_name):
    tag = session.query(Tag).filter(Tag.name==tag_name).one_or_none()
    if not tag:
        tag = Tag(name=tag_name)
        session.add(tag)
        session.flush()
    return tag

def get_or_create_tags(tag_names=[]):
    tags = []
    for tn in tag_names:
        tag = get_or_create_tag(tn)
        tags.append(tag)
    return tags
        
def get_tag_by_id(tag_id):
    tag = session.query(Tag).filter(Tag.id==tag_id).one_or_none();
    if not tag:
        raise InvalidTagIdError()
    return tag


