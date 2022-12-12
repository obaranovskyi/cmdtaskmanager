from .errors import InvalidCommentIdError
from ..task.errors import InvalidTaskIdError
from .core import update_comment as update_comment_fn
from ..shared.display import display_error


def update_comment(args):
    try:
        update_comment_fn(
            comment_id=args.comment_id,
            task_id=args.task_id,
            content=args.content
        )
    except (InvalidCommentIdError,
            InvalidTaskIdError)as e:
        display_error(e.message)
