from .add_tag import add_tag as add_tag_handler
from ..shared.parser import subparsers


def add_tag_subparser():
    add_tag = subparsers.add_parser('add-tag', help='Add tag.')
    add_tag.add_argument('name', type=str, help='tag name.')
    add_tag.add_argument('-d', '--description', type=str, required=False,
                          metavar='',
                          help='Tag description.')
    add_tag.set_defaults(func=add_tag_handler)
