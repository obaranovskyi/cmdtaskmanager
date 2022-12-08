from .display_tag_subparser import display_tag_subparser
from .display_tag_list_subparser import display_tag_list_subparser
from .add_tag_subparser import add_tag_subparser

def register_tag_subparsers():
    display_tag_subparser()
    display_tag_list_subparser()
    add_tag_subparser()
