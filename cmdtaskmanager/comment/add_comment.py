from ..task.errors import InvalidTaskIdError
from .core import create_comment
from ..shared.display import display_error


def add_comment(args):
    try:
        create_comment(
            task_id=args.task_id,
            content=args.content,
        )
    except InvalidTaskIdError as e:
        display_error(e.message)
