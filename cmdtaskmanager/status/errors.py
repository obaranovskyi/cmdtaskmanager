from ..shared.errors import InvalidIdError, InvalidNameError


entity_name = 'status'

class InvalidStatusIdError(InvalidIdError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

class InvalidStatusNameError(InvalidNameError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)
