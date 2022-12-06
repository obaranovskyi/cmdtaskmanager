from ..shared.errors import InvalidFinishDateError, InvalidIdError, InvalidNameError, EntityNameAlreadyExists


entity_name = 'task'

class InvalidTaskFinishDateError(InvalidFinishDateError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

class InvalidTaskIdError(InvalidIdError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

class InvalidTaskNameError(InvalidNameError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

class TaskNameAlreadyExists(EntityNameAlreadyExists):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

