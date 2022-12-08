from ..shared.consts import DEFAULT_DISPLAY_LIMIT
from .display_project_list import display_project_list as display_project_list_handler
from ..shared.parser import subparsers


def display_project_list_subparser():
    display_project_list = subparsers.add_parser('display-project-list', help='Display project list.')
    display_project_list.add_argument('-l', '--limit', type=int, required=False,
                          metavar='',
                          help="Amount of projects to display.",
                          default=DEFAULT_DISPLAY_LIMIT)
    # TODO: Here should be added the query functionality
    # to display project by project, priority, project and priority etc.
    display_project_list.set_defaults(func=display_project_list_handler)
