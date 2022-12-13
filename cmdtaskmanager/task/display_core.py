from rich import print
from rich.markdown import Markdown
from rich.tree import Tree
from rich.table import Table
from ..shared.consts import EMPTY_TABLE_CELL
from ..tag.display_core import get_display_tags_tree
from ..project.display_core import get_display_project_tree
from ..status.display_core import get_display_status
from ..shared.date_core import format_to_local_d, format_to_local_dt
from ..shared.display import GREEN, BLUE, GREY, RED, YELLOW, no_items_yet
import cmdtaskmanager.comment.core as comment_core
import cmdtaskmanager.comment.display_core as comment_display_core


def display_task(task):
    task_tree = get_display_task_tree(task)
    print(task_tree)

def get_display_task_tree(task):
    task_tree = Tree(f"[{BLUE}] Task:")
    task_tree.add(f'[{GREEN}] Id: [{BLUE}]{task.id}')
    task_tree.add(f'[{GREEN}] Title: [{BLUE}]{task.title}')
    if task.description:
        task_tree.add(f'[{GREEN}] Description: [{BLUE}]{task.description}')
    task_tree.add(f'[{GREEN}] Priority: [{BLUE}]{task.priority}')
    task_tree.add(get_display_status(task.status, True))
    task_tree.add(f'[{GREEN}] Date Created: [{BLUE}]{format_to_local_dt(task.date_created)}')
    if task.finish_date:
        task_tree.add(f'[{GREEN}] Finish Date: [{BLUE}]{format_to_local_d(task.finish_date)}')
    if task.project:
        task_tree.add(get_display_project_tree(task.project))
    if task.tags:
        task_tree.add(get_display_tags_tree(task.tags))
    comments = comment_core.get_comments_by_task_id(task.id)
    if comments:
        task_tree.add(comment_display_core.get_comments_tree_for_task(comments))
    if task.long_description:
        task_tree.add(f'[{GREEN}] Long Description: \n')
        task_tree.add(Markdown(task.long_description))
    return task_tree


def display_task_list(tasks):
    if not tasks:
        no_items_yet('tasks')
        return
    task_table = Table('Id', style=GREY, header_style=YELLOW)
    task_table.add_column('Title', style=GREEN)
    task_table.add_column('Priority', style=BLUE)
    task_table.add_column('Status')
    task_table.add_column('Project', style=BLUE)
    task_table.add_column('Tags', style=GREEN)
    task_table.add_column('Finish Date', style=RED)
    for t in tasks:
        project_name = t.project.name if t.project else EMPTY_TABLE_CELL
        tags = ", ".join([tt.name for tt in t.tags]) if t.tags else EMPTY_TABLE_CELL 
        finish_date = format_to_local_d(t.finish_date) if t.finish_date else EMPTY_TABLE_CELL 
        task_table.add_row(
            str(t.id),
            t.title,
            str(t.priority),
            get_display_status(t.status),
            project_name,
            tags,
            finish_date
        )
    print(task_table)
