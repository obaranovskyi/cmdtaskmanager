from .remove_task_subparser import remove_task_subparser
from .add_task_subparser import add_task_subparser

def register_task_subparsers():
    add_task_subparser()
    remove_task_subparser()
