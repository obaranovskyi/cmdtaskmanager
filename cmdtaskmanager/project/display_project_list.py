from .core import get_projects_to_display
from .display_core import display_project_list as display_project_list_fn


def display_project_list(args):
    display_project_list_fn(get_projects_to_display(args.limit))
