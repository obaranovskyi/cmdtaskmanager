from ..shared.display import display_error
from .errors import InvalidTagIdError
from .core import get_tag_by_id
from .display_core import display_tag as display_tag_fn


def display_tag(args):
    try:
        tag = get_tag_by_id(args.tag_id)
        display_tag_fn(tag)
    except InvalidTagIdError as e:
        display_error(e.message)
