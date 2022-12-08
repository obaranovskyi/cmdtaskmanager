from .models import StatusModel
from ..shared.display import BLUE, GREEN, GREY, RED, YELLOW


NOT_STARTED = StatusModel('Not Started', 'The task is not started yet.', GREY)
IN_PROGRESS = StatusModel('In progress', 'The task is in progress.', BLUE)
POSTPONED = StatusModel('Postponed', 'The task is postponed.', YELLOW)
REMOVED = StatusModel('Removed', 'The task is removed as it\'s not relevant anymore.', RED)
COMPLETED = StatusModel('Completed', 'The task is done.', GREEN)

STATUSES = [
    NOT_STARTED, IN_PROGRESS,
    COMPLETED, POSTPONED, REMOVED]
