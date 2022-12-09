from ..shared.errors import EntityNameAlreadyExists, InvalidIdError


entity_name = 'tag'

class InvalidTagIdError(InvalidIdError):
    def __init__(self):
        super().__init__(entity_name)

class TagNameAlreadyExists(EntityNameAlreadyExists):
    def __init__(self):
        super().__init__(entity_name)

