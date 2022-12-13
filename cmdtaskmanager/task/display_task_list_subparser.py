from ..shared.consts import DEFAULT_DISPLAY_LIMIT
from .display_task_list import display_task_list as display_task_list_handler
from ..shared.parser import subparsers


def display_task_list_subparser():
    display_task_list = subparsers.add_parser('display-task-list', help='Display task list.')
    display_task_list.add_argument('-l', '--limit', type=int, required=False,
                          metavar='',
                          help="Amount of tasks to display.",
                          default=DEFAULT_DISPLAY_LIMIT)
    # project exclusive group
    add_task_project = display_task_list.add_mutually_exclusive_group(required=False)
    add_task_project.add_argument('-pn', '--project-name', type=str, required=False,
                          metavar='',
                          help='Search by project name.')
    add_task_project.add_argument('-pi', '--project-id', type=int, required=False,
                          metavar='',
                          help='Search by project id.')
    display_task_list.set_defaults(func=display_task_list_handler)
