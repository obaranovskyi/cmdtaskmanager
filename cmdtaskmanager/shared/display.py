from rich import print


BLUE = "turquoise2"
RED = "deep_pink2"
GREEN = "spring_green1"
YELLOW = "yellow"
GREY = "#BEBEBE"

def display_info(message):
    print(f"[{BLUE}]{message}")

def display_error(message):
    print(f"[{RED}]{message}")


def no_items_yet(plural_entity_name):
    display_error(f"No {plural_entity_name} yet.")
