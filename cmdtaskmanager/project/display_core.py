from rich.tree import Tree
from rich import print
from ..shared.date_core import format_to_local_d
from ..shared.display import GREEN, BLUE


def display_project(project):
    project_tree = get_display_project_tree(project)
    print(project_tree)

def get_display_project_tree(project):
    project_tree = Tree(f'[{BLUE}] Project:')
    project_tree.add(f'[{GREEN}] Id: [{BLUE}]{project.id}')
    project_tree.add(f'[{GREEN}] Name: [{BLUE}]{project.name}')
    project_tree.add(f'[{GREEN}] Description: [{BLUE}]{project.description}')
    if project.finish_date:
        project_tree.add(f'[{GREEN}] Finish Date: [{BLUE}]{format_to_local_d(project.finish_date)}')
    return project_tree

