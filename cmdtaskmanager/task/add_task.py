from ..tag.errors import InvalidTagIdError
from ..project.errors import InvalidProjectIdError, InvalidProjectNameError
from ..shared.errors import IsNotFileError, NoSuchFileError
from .errors import InvalidTaskFinishDateError
from .core import create_task
from ..shared.display import display_error


def add_task(args):
    try:
        create_task(
            title=args.title,
            priority=args.priority,
            description=args.description,
            long_description=args.long_description,
            finish_date=args.finish_date,
            project_name=args.project_name,
            project_id=args.project_id,
            tag_names=args.tag_names,
            tag_ids=args.tag_ids
        )
    except (InvalidTaskFinishDateError,
            NoSuchFileError,
            IsNotFileError,
            InvalidProjectIdError,
            InvalidProjectNameError,
            InvalidTagIdError) as e:
        display_error(e.message)
