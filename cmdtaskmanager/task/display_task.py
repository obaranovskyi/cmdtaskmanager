from ..shared.display import display_error
from .errors import InvalidTaskIdError
from .core import get_task_by_id
from .display_core import display_task as display_task_fn


def display_task(args):
    try:
        task = get_task_by_id(args.task_id)
        display_task_fn(task)
    except InvalidTaskIdError as e:
        display_error(e.message)
