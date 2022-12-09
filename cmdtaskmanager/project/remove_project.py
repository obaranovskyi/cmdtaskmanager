from ..shared.display import display_error
from .errors import InvalidProjectIdError, ProjectHasTaskDependencies 
from .core import remove_project as remove_project_fn


def remove_project(args):
    try:
        remove_project_fn(args.project_id)
    except InvalidProjectIdError as e:
        display_error(e.message)
    except ProjectHasTaskDependencies as e:
        display_error(e.message)
        e.display_dependencies()
    

