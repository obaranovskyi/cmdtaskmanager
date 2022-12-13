from .core import get_tasks_to_display
from .display_core import display_task_list as display_task_list_fn


def display_task_list(args):
    tasks_to_display = get_tasks_to_display(
        limit=args.limit,
        project_name=args.project_name,
        project_id=args.project_id,
        tag_names=args.tag_names,
        tag_ids=args.tag_ids
    )
    display_task_list_fn(tasks_to_display)
