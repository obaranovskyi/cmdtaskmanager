from .display_tag import display_tag as display_tag_handler
from ..shared.parser import subparsers


def display_tag_subparser():
    add_tag = subparsers.add_parser('display-tag', help='Display tag.')
    add_tag.add_argument('tag_id', type=int, help='tag id.')
    add_tag.set_defaults(func=display_tag_handler)
