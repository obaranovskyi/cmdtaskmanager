from .core import create_task
from ..shared.display import display_error


def add_task(args):
    try:
        create_task(
            title=args.title,
            priority=args.priority,
            description=args.description,
            long_description=args.long_description,
            finish_date=args.finish_date,
            project_name=args.project_name,
            project_id=args.project_id,
        )
    except Exception as e:
        display_error(e.message)
