from ..shared.errors import EntityNameAlreadyExists, InvalidIdError, InvalidFinishDateError, InvalidNameError


entity_name = 'project'

class InvalidProjectFinishDateError(InvalidFinishDateError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

class InvalidProjectIdError(InvalidIdError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

class InvalidProjectNameError(InvalidNameError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

class ProjectNameAlreadyExists(EntityNameAlreadyExists):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)


