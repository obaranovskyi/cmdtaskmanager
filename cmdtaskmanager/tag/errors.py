from ..shared.errors import EntityNameAlreadyExists, InvalidIdError


entity_name = 'tag'

class InvalidTagIdError(InvalidIdError):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

class TagNameAlreadyExists(EntityNameAlreadyExists):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

