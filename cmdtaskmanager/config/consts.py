import os

from .models import DefaultConfigurations

VERSION = '0.0.1'
USER_HOME_DIR = os.path.expanduser('~')

CONFIG_FILENAME = 'config.json'
CONFIG_DIR = f"{USER_HOME_DIR}/.config/cmdtaskmanager"
CONFIG_LOCATION = f"{CONFIG_DIR}/{CONFIG_FILENAME}"

DB_NAME = 'cmdtaskmanager'
DB_LOCATION = f"{CONFIG_DIR}/{DB_NAME}.sqlite"

DEFAULT_CONFIG = DefaultConfigurations([])
