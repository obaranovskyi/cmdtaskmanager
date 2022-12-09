from .remove_tag import remove_tag as remove_tag_handler
from ..shared.parser import subparsers


def remove_tag_subparser():
    add_tag = subparsers.add_parser('remove-tag', help='Remove tag.')
    add_tag.add_argument('tag_id', type=int, help='tag id.')
    add_tag.set_defaults(func=remove_tag_handler)
