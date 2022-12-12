from rich import print
from rich.tree import Tree
from ..shared.display import BLUE, GREEN


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
