from ..task.display_core import display_task_list
from ..shared.errors import EntityHasDependencyError, EntityNameAlreadyExists, InvalidIdError


entity_name = 'tag'

class InvalidTagIdError(InvalidIdError):
    def __init__(self):
        super().__init__(entity_name)

class TagNameAlreadyExists(EntityNameAlreadyExists):
    def __init__(self):
        super().__init__(entity_name)

class TagHasTaskDependencies(EntityHasDependencyError):
    def __init__(self, entities):
        super().__init__(entity_name, entities, display_task_list)
