import sys

from .config.core import setup_config
from .project.entities import *
from .status.entities import *
from .tag.entities import *
from .comment.entities import *
from .task.entities import *
from .database.db_manager import db
from .status.core import setup_base_statuses
from .status.subparsers import register_status_subparsers
from .comment.subparsers import register_comment_subparsers
from .tag.subparsers import register_tag_subparsers
from .project.subparsers import register_project_subparsers
from .task.subparsers import register_task_subparsers
from .shared.parser import parser


def set_default_to_help():
    if len(sys.argv) == 1:
        sys.argv.append('-h')

def setup():
    setup_config()
    setup_base_statuses()

def register_subparsers():
    register_project_subparsers()
    register_task_subparsers()
    register_tag_subparsers()
    register_status_subparsers()
    register_comment_subparsers()

def main():
    set_default_to_help()
    setup()
    register_subparsers()
    args = parser.parse_args()
    args.func(args)
    db.end_session()


if __name__ == '__main__':
    main()
