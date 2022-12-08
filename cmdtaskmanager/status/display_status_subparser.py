from .display_status import display_status as display_status_handler
from ..shared.parser import subparsers


def display_status_subparser():
    add_status = subparsers.add_parser('display-status', help='Display status.')
    add_status.add_argument('status_id', type=int, help='status id.')
    add_status.set_defaults(func=display_status_handler)
