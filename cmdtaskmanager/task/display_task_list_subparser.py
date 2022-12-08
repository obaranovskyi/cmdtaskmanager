from ..shared.consts import DEFAULT_DISPLAY_LIMIT
from .display_task_list import display_task_list as display_task_list_handler
from ..shared.parser import subparsers


def display_task_list_subparser():
    display_task_list = subparsers.add_parser('display-task-list', help='Display task list.')
    display_task_list.add_argument('-l', '--limit', type=int, required=False,
                          metavar='',
                          help="Amount of tasks to display.",
                          default=DEFAULT_DISPLAY_LIMIT)
    # TODO: Here should be added the query functionality
    # to display task by project, priority, project and priority etc.
    display_task_list.set_defaults(func=display_task_list_handler)
