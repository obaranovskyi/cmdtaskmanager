from ..shared.parser import subparsers
from .update_task_status import (reset_task, start_task, complete_task,
                                 remove_task, postpone_task)


def reset_task_subparser():
    update_task = subparsers.add_parser('reset-task', help='Update task status to \'Not Started\'.')
    update_task.add_argument('task_id', type=str, help='Id of the task whose status should be updated.')
    update_task.set_defaults(func=reset_task)

def start_task_subparser():
    update_task = subparsers.add_parser('start-task', help='Update task status to \'In Progress\'.')
    update_task.add_argument('task_id', type=str, help='Id of the task whose status should be updated.')
    update_task.set_defaults(func=start_task)

def complete_task_subparser():
    update_task = subparsers.add_parser('complete-task', help='Update task status to \'Completed\'.')
    update_task.add_argument('task_id', type=str, help='Id of the task whose status should be updated.')
    update_task.set_defaults(func=complete_task)

def remove_task_subparser():
    update_task = subparsers.add_parser('remove-task', help='Update task status to \'Removed\'.')
    update_task.add_argument('task_id', type=str, help='Id of the task whose status should be updated.')
    update_task.set_defaults(func=remove_task)

def postpone_task_subparser():
    update_task = subparsers.add_parser('postpone-task', help='Update task status to \'Postpone\'.')
    update_task.add_argument('task_id', type=str, help='Id of the task whose status should be updated.')
    update_task.set_defaults(func=postpone_task)
