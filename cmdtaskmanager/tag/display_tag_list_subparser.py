from ..shared.consts import DEFAULT_DISPLAY_LIMIT
from .display_tag_list import display_tag_list as display_tag_list_handler
from ..shared.parser import subparsers


def display_tag_list_subparser():
    display_tag_list = subparsers.add_parser('display-tag-list', help='Display tag list.')
    display_tag_list.add_argument('-l', '--limit', type=int, required=False,
                          metavar='',
                          help="Amount of tags to display.",
                          default=DEFAULT_DISPLAY_LIMIT)
    display_tag_list.set_defaults(func=display_tag_list_handler)
