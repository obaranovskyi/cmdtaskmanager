from .remove_task_subparser import remove_task_subparser
from .add_task_subparser import add_task_subparser
from ..shared.parser import subparsers

def register_task_subparsers():
    add_task_subparser(subparsers)
    remove_task_subparser(subparsers)
