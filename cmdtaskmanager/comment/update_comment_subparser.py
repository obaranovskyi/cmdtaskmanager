from .update_comment import update_comment as update_comment_handler
from ..shared.parser import subparsers


def update_comment_subparser():
    update_comment = subparsers.add_parser('update-comment', help='Update comment.')
    update_comment.add_argument('comment_id', type=str, help='Comment id.')
    update_comment.add_argument('-t', '--task-id', type=str, required=False,
                                metavar='', help='Task id to which comment is related.')
    update_comment.add_argument('-c', '--content', type=str, required=False,
                                metavar='', help='Comment content.')
    update_comment.set_defaults(func=update_comment_handler)
