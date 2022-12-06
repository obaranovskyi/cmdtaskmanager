from .display_task_subparser import display_task_subparser
from .remove_task_subparser import remove_task_subparser
from .add_task_subparser import add_task_subparser

def register_task_subparsers():
    display_task_subparser()
    add_task_subparser()
    remove_task_subparser()
