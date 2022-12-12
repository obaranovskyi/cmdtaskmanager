# from .display_comment_list_subparser import display_comment_list_subparser
# from .display_comment_subparser import display_comment_subparser
from .remove_comment_subparser import remove_comment_subparser
from .add_comment_subparser import add_comment_subparser
from .update_comment_subparser import update_comment_subparser

def register_comment_subparsers():
    # display_comment_subparser()
    # display_comment_list_subparser()
    add_comment_subparser()
    update_comment_subparser()
    remove_comment_subparser()
