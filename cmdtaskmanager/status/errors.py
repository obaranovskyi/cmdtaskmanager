from ..shared.errors import InvalidIdError


entity_name = 'status'

class InvalidStatusIdError(InvalidIdError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

