from .add_comment import add_comment as add_comment_handler
from ..shared.parser import subparsers


def add_comment_subparser():
    add_comment = subparsers.add_parser('add-comment', help='Add comment.')
    add_comment.add_argument('task_id', type=str, help='Task id to which to add a comment.')
    add_comment.add_argument('content', type=str, help='Comment content.')
    add_comment.set_defaults(func=add_comment_handler)
