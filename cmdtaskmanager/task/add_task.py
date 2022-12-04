from .status_core import get_status_by_name
from .consts import NOT_STARTED
from .entities import Task
from ..database.db_manager import session


def add_task(args):
    # TODO: here check if long_description is actually file and
    # if it's possible to read its content

    # TODO: check if project exists firsts
    # should be search by name or by id
    # for this might be used exclusive argparse group
    # to except either project-id or project-name

    # TODO: parse finish_date till passing it to the Task object

    not_started = get_status_by_name(NOT_STARTED)

    task = Task(
        title=args.title,
        priority=args.priority,
        description=args.description,
        # TODO: this has be read from the file
        # long_description=long_description,
        status=not_started,
    )

    # here id is not yet available
    session.add(task)
    print('before', task)

    # after flush id will be available
    session.flush()
    print('after', task)
