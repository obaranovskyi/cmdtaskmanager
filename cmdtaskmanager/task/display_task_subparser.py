from .display_task import display_task as display_task_handler
from ..shared.parser import subparsers


def display_task_subparser():
    add_task = subparsers.add_parser('display-task', help='Display task.')
    add_task.add_argument('task_id', type=int, help='Task id.')
    add_task.set_defaults(func=display_task_handler)
