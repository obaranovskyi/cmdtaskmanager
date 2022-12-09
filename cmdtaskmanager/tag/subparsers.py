from .display_tag_subparser import display_tag_subparser
from .display_tag_list_subparser import display_tag_list_subparser
from .add_tag_subparser import add_tag_subparser
from .update_tag_subparser import update_tag_subparser
from .remove_tag_subparser import remove_tag_subparser

def register_tag_subparsers():
    display_tag_subparser()
    display_tag_list_subparser()
    add_tag_subparser()
    update_tag_subparser()
    remove_tag_subparser()
