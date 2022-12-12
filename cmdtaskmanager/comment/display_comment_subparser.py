from .display_comment import display_comment as display_comment_handler
from ..shared.parser import subparsers


def display_comment_subparser():
    display_comment = subparsers.add_parser('display-comment', help='Display comment.')
    display_comment.add_argument('comment_id', type=str, help='Comment id.')
    display_comment.set_defaults(func=display_comment_handler)
