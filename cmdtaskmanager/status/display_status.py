from ..shared.display import display_error
from .errors import InvalidStatusIdError
from .core import get_status_by_id
from .display_core import display_status as display_status_fn


def display_status(args):
    try:
        status = get_status_by_id(args.status_id)
        display_status_fn(status)
    except InvalidStatusIdError as e:
        display_error(e.message)
