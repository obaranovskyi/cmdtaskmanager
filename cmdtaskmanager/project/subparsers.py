from .display_project_subparser import display_project_subparser
from .add_project_subparser import add_project_subparser

def register_project_subparsers():
    display_project_subparser()
    add_project_subparser()
