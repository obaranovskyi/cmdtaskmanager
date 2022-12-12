from .core import get_comments_by_task_id
from .display_core import display_comment_list as display_comment_list_fn


def display_comment_list(args):
    comments = get_comments_by_task_id(args.task_id)
    display_comment_list_fn(comments)
