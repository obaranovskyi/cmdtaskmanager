from .display_tag_subparser import display_tag_subparser
from .add_tag_subparser import add_tag_subparser

def register_tag_subparsers():
    display_tag_subparser()
    add_tag_subparser()
