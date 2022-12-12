from .core import get_comment_by_id
from .errors import InvalidCommentIdError
from .display_core import display_comment as display_comment_fn
from ..shared.display import display_error


def display_comment(args):
    try:
        comment = get_comment_by_id(args.comment_id)
        display_comment_fn(comment)
    except InvalidCommentIdError as e:
        display_error(e.message)
