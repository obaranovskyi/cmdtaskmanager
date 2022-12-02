from .add_task_subparser import add_task_subparser

def register_task_subparsers(subparsers):
    add_task_subparser(subparsers)
