from ..status.errors import InvalidStatusIdError, InvalidStatusNameError
from .errors import InvalidProjectFinishDateError, InvalidProjectIdError, ProjectNameAlreadyExists
from .core import update_project as update_project_fn
from ..shared.display import display_error


def update_project(args):
    try:
        update_project_fn(
            project_id=args.id,
            name=args.name,
            description=args.description,
            finish_date=args.finish_date,
            status_id=args.status_id,
            status_name=args.status_name
        )
    except (InvalidProjectIdError,
            InvalidProjectFinishDateError,
            ProjectNameAlreadyExists,
            InvalidStatusIdError,
            InvalidStatusNameError) as e:
        display_error(e.message)
