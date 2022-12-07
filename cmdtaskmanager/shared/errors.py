class InvalidFinishDateError(Exception):
    """An exception is raised when the finish date is later than now.

    Attributes:
        entity_name -- Entity name for which current exception is raised. 
    """
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.message = f'Invalid date. A {entity_name} finish date should be later than now.'
        super().__init__(self.message)


class InvalidIdError(Exception):
    """An exception is raised when the given id doesn't exist.

    Attributes:
        entity_name -- Entity name for which current exception is raised. 
    """
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.message = f'Invalid id. The {entity_name} with such an id doesn\'t exist.'
        super().__init__(self.message)


class InvalidNameError(Exception):
    """An exception is raised when the given name doesn't exist.

    Attributes:
        entity_name -- Entity name for which current exception is raised. 
    """
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.message = f'Invalid name. The {entity_name} with such a name doesn\'t exist.'
        super().__init__(self.message)


class EntityNameAlreadyExists(Exception):
    """An exception is raised when the given name already exists, but it has to be unique.

    Attributes:
        entity_name -- Entity name for which current exception is raised. 
    """
    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.message = f'Given {entity_name} name is invalid. ' + \
                       f'Most likely, the {entity_name} with such a name already exists.'
        super().__init__(self.message)


class NoSuchFileError(Exception):
    """An exception is raised when the given file doesn't exist.

    Attributes:
        filename -- The filename that was given.
    """
    def __init__(self, filename):
        self.filename = filename
        self.message = f'The file with the name {self.filename} doesn\'t exist.'
        super().__init__(self.message)


class IsNotFileError(Exception):
    """An exception is raised when the given file is not readable.

    Attributes:
        filename -- The filename that was given.
    """
    def __init__(self, filename):
        self.filename = filename
        self.message = f'The file with the name {self.filename} is not readable.'
        super().__init__(self.message)


        
