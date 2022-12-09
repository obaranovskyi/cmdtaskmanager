from ..shared.display import display_error
from .errors import InvalidTaskIdError
from .core import remove_task as remove_task_fn


def remove_task(args):
    try:
        remove_task_fn(args.task_id)
    except InvalidTaskIdError as e:
        display_error(e.message)
    

