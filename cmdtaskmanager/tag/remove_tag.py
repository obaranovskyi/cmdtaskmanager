from ..shared.display import display_error
from .errors import InvalidTagIdError, TagHasTaskDependencies
from .core import remove_tag as remove_tag_fn


def remove_tag(args):
    try:
        remove_tag_fn(args.tag_id)
    except InvalidTagIdError as e:
        display_error(e.message)
    except TagHasTaskDependencies as e:
        display_error(e.message)
        e.display_dependencies()
    

