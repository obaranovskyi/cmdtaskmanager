from ..shared.display import display_error
from .errors import InvalidTagIdError, TagNameAlreadyExists
from .core import update_tag as update_tag_fn


def update_tag(args):
    try:
        update_tag_fn(
            tag_id=args.id,
            name=args.name,
            description=args.description,
        )
    except (InvalidTagIdError,
            TagNameAlreadyExists) as e:
        display_error(e.message)
