from .remove_comment import remove_comment as remove_comment_handler
from ..shared.parser import subparsers


def remove_comment_subparser():
    remove_comment = subparsers.add_parser('remove-comment', help='Remove comment.')
    remove_comment.add_argument('comment_id', type=str, help='Comment id.')
    remove_comment.set_defaults(func=remove_comment_handler)
