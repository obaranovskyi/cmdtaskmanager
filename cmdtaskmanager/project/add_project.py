from .core import create_project
from ..shared.display import display_error


def add_project(args):
    try:
        create_project(
            name=args.name,
            description=args.description,
            finish_date=args.finish_date
        )
    except Exception as e:
        display_error(e.message)
