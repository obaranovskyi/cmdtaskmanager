from .models import StatusModel
from ..shared.display import BLUE, GREEN, GREY, RED, YELLOW


NOT_STARTED = StatusModel('Not Started', 'The task is not started yet.', f'[{GREY}]')
IN_PROGRESS = StatusModel('In progress', 'The task is in progress.', f'[{BLUE}]')
POSTPONED = StatusModel('Postponed', 'The task is postponed.', f'[{YELLOW}]')
REMOVED = StatusModel('Removed', 'The task is removed as it\'s not relevant anymore.', f'[{RED}]')
COMPLETED = StatusModel('Completed', 'The task is done.', f'[{GREEN}]')


STATUSES = [
    NOT_STARTED, IN_PROGRESS,
    POSTPONED, REMOVED, COMPLETED]
