from .update_tag import update_tag as update_tag_handler
from ..shared.parser import subparsers


def update_tag_subparser():
    update_tag = subparsers.add_parser('update-tag', help='Update tag.')
    update_tag.add_argument('id', type=str, help='Tag id.')
    update_tag.add_argument('-n', '--name', type=str, required=False,
                          metavar='', help='Tag name.')
    update_tag.add_argument('-d', '--description', type=str, required=False,
                          metavar='', help='Tag description.')
    update_tag.set_defaults(func=update_tag_handler)
