from .errors import InvalidCommentIdError
from .core import remove_comment as remove_comment_fn
from ..shared.display import display_error


def remove_comment(args):
    try:
        remove_comment_fn(
            comment_id=args.comment_id
        )
    except InvalidCommentIdError as e:
        display_error(e.message)
