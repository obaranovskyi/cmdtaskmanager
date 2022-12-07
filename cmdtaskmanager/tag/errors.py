from ..shared.errors import EntityNameAlreadyExists


entity_name = 'tag'

class TagNameAlreadyExists(EntityNameAlreadyExists):
    def __init__(self):
        self.entity_name = entity_name
        super().__init__(self.entity_name)

