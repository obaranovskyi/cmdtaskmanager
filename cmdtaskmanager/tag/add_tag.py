from ..shared.display import display_error
from .errors import TagNameAlreadyExists
from .core import create_tag


def add_tag(args):
    try:
        create_tag(
            name=args.name,
            description=args.description,
        )
    except TagNameAlreadyExists as e:
        display_error(e.message)
