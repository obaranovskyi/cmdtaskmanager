from ..shared.errors import InvalidIdError, InvalidNameError


entity_name = 'status'

class InvalidStatusIdError(InvalidIdError):
    def __init__(self):
        super().__init__(entity_name)

class InvalidStatusNameError(InvalidNameError):
    def __init__(self):
        super().__init__(entity_name)
