from .config.core import setup_config
from .project.entities import *
from .tag.entities import *
from .task.entities import *
from .database.db_manager import db
from .task.status_core import setup_base_statuses
from .task.subparsers import register_task_subparsers
from .shared.parser import parser


def main():
    setup_config()
    setup_base_statuses()
    register_task_subparsers()
    args = parser.parse_args()
    args.func(args)
    db.end_session()


if __name__ == '__main__':
    main()
