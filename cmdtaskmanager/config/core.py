import os
from cmdtaskmanager.shared.json_file import write_json
from .consts import CONFIG_LOCATION, DEFAULT_CONFIG

def setup_config():
    if os.path.exists(CONFIG_LOCATION): return
    os.makedirs(os.path.dirname(CONFIG_LOCATION), exist_ok=True)
    write_json(CONFIG_LOCATION, DEFAULT_CONFIG.configs_as_dict())
