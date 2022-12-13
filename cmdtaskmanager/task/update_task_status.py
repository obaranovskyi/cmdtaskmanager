from .core import update_task_status as update_task_status_fn
from .errors import InvalidTaskIdError
from ..shared.display import display_error
from ..status.errors import InvalidStatusNameError
from ..status.consts import (NOT_STARTED, IN_PROGRESS, COMPLETED,
                             REMOVED, POSTPONED)

def reset_task(args):
    update_task_status(args.task_id, NOT_STARTED.name)

def start_task(args):
    update_task_status(args.task_id, IN_PROGRESS.name)
    
def complete_task(args):
    update_task_status(args.task_id, COMPLETED.name)

def remove_task(args):
    update_task_status(args.task_id, REMOVED.name)

def postpone_task(args):
    update_task_status(args.task_id, POSTPONED.name)

def update_task_status(task_id, status_name):
    try:
        update_task_status_fn(
            task_id=task_id,
            status_name=status_name
        )
    except (InvalidTaskIdError,
            InvalidStatusNameError) as e:
        display_error(e.message)
