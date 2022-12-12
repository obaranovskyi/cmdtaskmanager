from ..shared.errors import InvalidIdError


entity_name = 'comment'

class InvalidCommentIdError(InvalidIdError):
    def __init__(self):
        super().__init__(entity_name)
