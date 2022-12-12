from .display_comment_list import display_comment_list as display_comment_list_handler
from ..shared.parser import subparsers


def display_comment_list_subparser():
    display_comment_list = subparsers.add_parser('display-comment-list', help='Display comment list.')
    display_comment_list.add_argument('task_id', type=str, help='Task id of the comments to display.')
    display_comment_list.set_defaults(func=display_comment_list_handler)
