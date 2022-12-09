from .remove_project import remove_project as remove_project_handler
from ..shared.parser import subparsers


def remove_project_subparser():
    add_project = subparsers.add_parser('remove-project', help='Remove project.')
    add_project.add_argument('project_id', type=int, help='Project id.')
    add_project.set_defaults(func=remove_project_handler)
