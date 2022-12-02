import os
import json


def write_json(file_location, json_content):
    if not os.path.exists(file_location):
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, 'w') as file_object:
        json.dump(json_content, file_object, indent=4)
