from .consts import STATUS_COLORS


def get_status_to_display(status):
    return f'{STATUS_COLORS[status.name]}{status.name}'
