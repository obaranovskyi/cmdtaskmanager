from .display_status_list_subparser import display_status_list_subparser
from .display_status_subparser import display_status_subparser

def register_status_subparsers():
    display_status_list_subparser()
    display_status_subparser()
