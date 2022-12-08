from .core import get_tags_to_display
from .display_core import display_tag_list as display_tag_list_fn


def display_tag_list(args):
    display_tag_list_fn(get_tags_to_display(args.limit))
