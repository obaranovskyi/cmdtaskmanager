from rich.table import Table
from rich import print
from rich.tree import Tree

from ..shared.date_core import format_to_local_dt
from .consts import STATUSES
from ..shared.display import BLUE, GREEN, GREY, YELLOW, no_items_yet


def get_display_status(status, include_label=False):
    label = f'[{GREEN}] Status: ' if include_label else ''
    sm = get_display_status_model_by_name(status.name)
    return f'{label}[{sm.color}]{status.name}'

def display_status(status):
    status_tree = get_display_status_tree(status)
    print(status_tree)

def get_display_status_tree(status):
    status_tree = Tree(f"[{BLUE}] Status:")
    status_tree.add(f'[{GREEN}] Id: [{BLUE}]{status.id}')
    status_tree.add(f'[{GREEN}] Name: [{get_display_status_model_by_name(status.name).color}]{status.name}')
    status_tree.add(f'[{GREEN}] Description: [{BLUE}]{status.description}')
    status_tree.add(f'[{GREEN}] Date Created: [{BLUE}]{format_to_local_dt(status.date_created)}')
    return status_tree

def display_status_list(statuses):
    if not statuses:
        no_items_yet('statuses')
        return
    status_table = Table('Id', style=GREY, header_style=YELLOW)
    status_table.add_column('Name', style=GREEN)
    status_table.add_column('Description', style=BLUE)
    for s in statuses:
        status_table.add_row(
            str(s.id),
            get_display_status(s),
            s.description,
        )
    print(status_table)

def get_display_status_model_by_name(name):
    return next(s for s in STATUSES if s.name == name)

