from ..shared.display import display_error
from .core import get_project_by_id
from .display_core import display_project as display_project_fn


def display_project(args):
    try:
        project = get_project_by_id(args.project_id)
        display_project_fn(project)
    except Exception as e:
        display_error(e.message)
