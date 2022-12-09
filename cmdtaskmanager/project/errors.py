from ..task.display_core import display_task_list
from ..shared.errors import (EntityNameAlreadyExists, InvalidIdError,
                             InvalidFinishDateError, InvalidNameError,
                             EntityHasDependencyError)


entity_name = 'project'

class InvalidProjectFinishDateError(InvalidFinishDateError):
    def __init__(self):
        super().__init__(entity_name)

class InvalidProjectIdError(InvalidIdError):
    def __init__(self):
        super().__init__(entity_name)

class InvalidProjectNameError(InvalidNameError):
    def __init__(self):
        super().__init__(entity_name)

class ProjectNameAlreadyExists(EntityNameAlreadyExists):
    def __init__(self):
        super().__init__(entity_name)

class ProjectHasTaskDependencies(EntityHasDependencyError):
    def __init__(self, entities):
        super().__init__(entity_name, entities, display_task_list)
