from .core import get_tasks_to_display
from .display_core import display_task_list as display_task_list_fn


def display_task_list(_):
    display_task_list_fn(get_tasks_to_display(10))
