from cmdtaskmanager.shared.json_file import write_json
from .consts import CONFIG_LOCATION, DEFAULT_CONFIG

def setup_config():
    write_json(CONFIG_LOCATION, DEFAULT_CONFIG.configs_as_dict())
