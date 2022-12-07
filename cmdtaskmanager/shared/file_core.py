import os
import json

from .errors import IsNotFileError, NoSuchFileError


def write_json(file_location, json_content):
    if file_exists(file_location):
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, 'w') as file_object:
        json.dump(json_content, file_object, indent=4)

def file_exists(file_location):
    return os.path.exists(file_location)

def is_dir(file_or_dir_name):
    return os.path.isdir(file_or_dir_name)
        
def get_file_content(file_location):
    """
    Raises:
        - `NoSuchFileError` -- When a file that was given doesn't exist.
        - `IsNotFileError` -- When a file that was given isn't readable.
    """
    if not file_exists(file_location):
        raise NoSuchFileError(file_location)
    if is_dir(file_location):
        raise IsNotFileError(file_location)
    with open(file_location, 'r') as file_object:
        return file_object.read()
