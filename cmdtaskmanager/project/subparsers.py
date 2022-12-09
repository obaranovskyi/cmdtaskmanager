from .display_project_subparser import display_project_subparser
from .display_project_list_subparser import display_project_list_subparser
from .add_project_subparser import add_project_subparser
from .update_project_subparser import update_project_subparser

def register_project_subparsers():
    display_project_subparser()
    display_project_list_subparser()
    add_project_subparser()
    update_project_subparser()
