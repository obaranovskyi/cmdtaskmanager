from .remove_task import remove_task as remove_task_handler


def remove_task_subparser(subparsers):
    add_task = subparsers.add_parser('remove-task', help='Remove task.')
    add_task.add_argument('task_id', type=int, help='Task id.')
    add_task.set_defaults(func=remove_task_handler)
