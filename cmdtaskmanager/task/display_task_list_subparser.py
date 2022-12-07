from .display_task_list import display_task_list as display_task_list_handler
from ..shared.parser import subparsers


def display_task_list_subparser():
    display_task_list = subparsers.add_parser('display-task-list', help='Display task list.')
    # TODO: Here should be added the query functionality
    # to display task by project, priority, project and priority etc.
    display_task_list.set_defaults(func=display_task_list_handler)
