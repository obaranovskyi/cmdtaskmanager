from ..status.errors import InvalidStatusIdError, InvalidStatusNameError
from ..tag.errors import InvalidTagIdError
from ..project.errors import InvalidProjectIdError, InvalidProjectNameError
from ..shared.errors import IsNotFileError, NoSuchFileError
from .errors import InvalidTaskFinishDateError, InvalidTaskIdError
from .core import update_task as update_task_fn
from ..shared.display import display_error


def update_task(args):
    try:
        update_task_fn(
            task_id=args.id,
            title=args.title,
            priority=args.priority,
            description=args.description,
            status_name=args.status_name,
            status_id=args.status_id,
            long_description=args.long_description,
            finish_date=args.finish_date,
            project_name=args.project_name,
            project_id=args.project_id,
            tag_names=args.tag_names,
            tag_ids=args.tag_ids
        )
    except (InvalidTaskIdError,
            InvalidTaskFinishDateError,
            NoSuchFileError,
            IsNotFileError,
            InvalidProjectIdError,
            InvalidProjectNameError,
            InvalidTagIdError,
            InvalidStatusIdError,
            InvalidStatusNameError) as e:
        display_error(e.message)
