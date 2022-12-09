from rich.tree import Tree
from rich.table import Table
from rich import print
from ..shared.consts import EMPTY_TABLE_CELL
from ..status.display_core import get_display_status
from ..shared.date_core import format_to_local_d, format_to_local_dt
from ..shared.display import GREEN, BLUE, GREY, RED, YELLOW, no_items_yet


def display_project(project):
    project_tree = get_display_project_tree(project)
    print(project_tree)

def get_display_project_tree(project):
    project_tree = Tree(f'[{BLUE}] Project:')
    project_tree.add(f'[{GREEN}] Id: [{BLUE}]{project.id}')
    project_tree.add(f'[{GREEN}] Name: [{BLUE}]{project.name}')
    if project.description:
        project_tree.add(f'[{GREEN}] Description: [{BLUE}]{project.description}')
    project_tree.add(get_display_status(project.status, True))
    project_tree.add(f'[{GREEN}] Date Created: [{BLUE}]{format_to_local_dt(project.date_created)}')
    if project.finish_date:
        project_tree.add(f'[{GREEN}] Finish Date: [{BLUE}]{format_to_local_d(project.finish_date)}')
    return project_tree

def display_project_list(projects):
    if not projects:
        no_items_yet('projects')
        return
    project_table = Table('Id', style=GREY, header_style=YELLOW)
    project_table.add_column('Name', style=GREEN)
    project_table.add_column('Description', style=BLUE)
    project_table.add_column('Status')
    project_table.add_column('Finish Date', style=RED)
    for p in projects:
        finish_date = format_to_local_d(p.finish_date) if p.finish_date else EMPTY_TABLE_CELL
        project_table.add_row(
            str(p.id),
            p.name,
            p.description,
            get_display_status(p.status),
            finish_date
        )
    print(project_table)
