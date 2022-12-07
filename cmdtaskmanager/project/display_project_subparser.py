from .display_project import display_project as display_project_handler
from ..shared.parser import subparsers


def display_project_subparser():
    add_project = subparsers.add_parser('display-project', help='Display project.')
    add_project.add_argument('project_id', type=int, help='Project id.')
    add_project.set_defaults(func=display_project_handler)
