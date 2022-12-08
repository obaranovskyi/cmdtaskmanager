from rich import print
from ..shared.display import GREEN
from .consts import STATUS_COLORS


def get_display_status(status, include_label=False):
    label = f'[{GREEN}] Status: ' if include_label else ''
    return f'{label}{STATUS_COLORS[status.name]}{status.name}'

def display_status(status):
    print(f'[{GREEN}] Status: {STATUS_COLORS[status.name]}{status.name}')
