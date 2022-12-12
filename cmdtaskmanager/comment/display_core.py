from rich import print
from rich.table import Table
from rich.tree import Tree
from ..shared.display import BLUE, GREEN, GREY, YELLOW
from ..shared.date_core import format_to_local_dt


def display_comment(comment):
    comment_tree = get_display_comment_tree(comment)
    print(comment_tree)

def get_display_comment_tree(comment, include_task_id=True):
    comment_tree = Tree(f"[{BLUE}] Comment:")
    comment_tree.add(f'[{GREEN}] Id: [{BLUE}]{comment.id}')
    comment_tree.add(f'[{GREEN}] Content: [{BLUE}]{comment.content}')
    if include_task_id:
        comment_tree.add(f'[{GREEN}] Task Id: [{BLUE}]{comment.task_id}')
    return comment_tree

def display_comment_list(comments):
    if not comments:
        return comments
    comments_table = Table('Id', style=GREY, header_style=YELLOW)
    comments_table.add_column('Comment', style=BLUE)
    comments_table.add_column(f'Commented', style=GREEN)
    for c in comments:
        comments_table.add_row(
            str(c.id),
                c.content,
                format_to_local_dt(c.date_created)
        )
    print(comments_table)
