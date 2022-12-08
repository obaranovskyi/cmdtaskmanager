from rich.table import Table
from rich import print

from .consts import STATUSES
from ..shared.display import BLUE, GREEN, GREY, YELLOW, no_items_yet


def get_display_status(status, include_label=False):
    label = f'[{GREEN}] Status: ' if include_label else ''
    sm = get_display_status_model_by_name(status.name)
    return f'{label}[{sm.color}]{status.name}'

def display_status(status):
    sm = get_display_status_model_by_name(status.name)
    print(f'[{GREEN}] Status: [{sm.color}]{status.name}')

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

