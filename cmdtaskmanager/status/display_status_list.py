from .core import get_statuses_to_display
from .display_core import display_status_list as display_status_list_fn


def display_status_list(args):
    display_status_list_fn(get_statuses_to_display(args.limit))

