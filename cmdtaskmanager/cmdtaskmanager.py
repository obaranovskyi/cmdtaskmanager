from .config.core import setup_config
from .project.entities import *
from .status.entities import *
from .tag.entities import *
from .task.entities import *
from .database.db_manager import db
from .status.core import setup_base_statuses
from .project.subparsers import register_project_subparsers
from .task.subparsers import register_task_subparsers
from .shared.parser import parser


def setup():
    setup_config()
    setup_base_statuses()

def register_subparsers():
    register_project_subparsers()
    register_task_subparsers()

def main():
    setup()
    register_subparsers()
    args = parser.parse_args()
    args.func(args)
    db.end_session()


if __name__ == '__main__':
    main()
