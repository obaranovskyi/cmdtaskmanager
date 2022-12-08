from ..shared.consts import DEFAULT_DISPLAY_LIMIT
from .display_status_list import display_status_list as display_status_list_handler
from ..shared.parser import subparsers


def display_status_list_subparser():
    display_status_list = subparsers.add_parser('display-status-list', help='Display status list.')
    display_status_list.add_argument('-l', '--limit', type=int, required=False,
                          metavar='',
                          help="Amount of statuses to display.",
                          default=DEFAULT_DISPLAY_LIMIT)
    display_status_list.set_defaults(func=display_status_list_handler)
