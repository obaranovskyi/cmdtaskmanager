from rich import print
from rich.markdown import Markdown
from rich.tree import Tree
from ..project.display_core import get_display_project_tree
from ..status.display_core import get_display_status
from ..shared.date_core import format_to_local_d, format_to_local_dt
from ..shared.display import GREEN, BLUE


def display_task(task):
    task_tree = get_display_task_tree(task)
    print(task_tree)

def get_display_task_tree(task):
    task_tree = Tree(f"[{BLUE}] Task:")
    task_tree.add(f'[{GREEN}] Id: [{BLUE}]{task.id}')
    task_tree.add(f'[{GREEN}] Title: [{BLUE}]{task.title}')
    task_tree.add(f'[{GREEN}] Description: [{BLUE}]{task.description}')
    task_tree.add(f'[{GREEN}] Priority: [{BLUE}]{task.priority}')
    task_tree.add(get_display_status(task.status))
    task_tree.add(f'[{GREEN}] Date Created: [{BLUE}]{format_to_local_dt(task.date_created)}')
    if task.finish_date:
        task_tree.add(f'[{GREEN}] Finish Date: [{BLUE}]{format_to_local_d(task.finish_date)}')
    if task.project:
        task_tree.add(get_display_project_tree(task.project))
    if task.long_description:
        task_tree.add(f'[{GREEN}] Long Description: \n')
        task_tree.add(Markdown(task.long_description))
    return task_tree


