from rich import print
from rich.tree import Tree
from ..shared.display import GREEN, BLUE


def display_tag(tag):
    tag_tree = get_display_tag_tree(tag)
    print(tag_tree)

def get_display_tag_tree(tag):
    tag_tree = Tree(f"[{BLUE}] Tag:")
    tag_tree.add(f'[{GREEN}] Id: [{BLUE}]{tag.id}')
    tag_tree.add(f'[{GREEN}] Name: [{BLUE}]{tag.name}')
    return tag_tree

def get_display_tags_tree(tags):
    tags_tree = Tree(f'[{BLUE}] Tags:')
    for tag in tags:
        tags_tree.add(get_display_tag_tree(tag))
    return tags_tree
    
