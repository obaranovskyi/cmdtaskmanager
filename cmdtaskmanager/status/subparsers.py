from .display_status_list_subparser import display_status_list_subparser

def register_status_subparsers():
    display_status_list_subparser()
