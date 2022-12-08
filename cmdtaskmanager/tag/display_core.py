from rich import print
from rich.table import Table
from rich.tree import Tree
from ..shared.date_core import format_to_local_dt
from ..shared.display import GREEN, BLUE, GREY, YELLOW, no_items_yet


def display_tag(tag):
    tag_tree = get_display_tag_tree(tag)
    print(tag_tree)

def get_display_tag_tree(tag):
    tag_tree = Tree(f"[{BLUE}] Tag:")
    tag_tree.add(f'[{GREEN}] Id: [{BLUE}]{tag.id}')
    tag_tree.add(f'[{GREEN}] Name: [{BLUE}]{tag.name}')
    if tag.description:
        tag_tree.add(f'[{GREEN}] Description: [{BLUE}]{tag.description}')
    tag_tree.add(f'[{GREEN}] Date Created: [{BLUE}]{format_to_local_dt(tag.date_created)}')
    return tag_tree

def get_display_tags_tree(tags):
    tags_tree = Tree(f'[{BLUE}] Tags:')
    for tag in tags:
        tags_tree.add(get_display_tag_tree(tag))
    return tags_tree
    
def display_tag_list(tags):
    if not tags:
        no_items_yet('tags')
        return
    tag_table = Table('Id', style=GREY, header_style=YELLOW)
    tag_table.add_column('Name', style=GREEN)
    tag_table.add_column('Description', style=BLUE)
    for p in tags:
        tag_table.add_row(
            str(p.id),
            p.name,
            p.description,
        )
    print(tag_table)
