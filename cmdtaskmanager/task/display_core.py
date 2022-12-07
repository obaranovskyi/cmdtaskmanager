from rich import print
from rich.console import Console
from rich.markdown import Markdown

from ..status.display_core import get_status_to_display
from ..shared.date_core import format_to_local_d, format_to_local_dt
from ..shared.display import GREEN, BLUE

def display_task(task):
    print(f'[{GREEN}] Id: [{BLUE}]{task.id}')
    print(f'[{GREEN}] Title: [{BLUE}]{task.title}')
    print(f'[{GREEN}] Description: [{BLUE}]{task.description}')
    print(f'[{GREEN}] Priority: [{BLUE}]{task.priority}')
    print(f'[{GREEN}] Status: ' + f'{get_status_to_display(task.status)}')
    print(f'[{GREEN}] Date Created: [{BLUE}]{format_to_local_dt(task.date_created)}')
    if task.finish_date:
        print(f'[{GREEN}] Finish Date: [{BLUE}]{format_to_local_d(task.finish_date)}')
    print(f'[{GREEN}] Long Description: \n')
    display_long_description(task.long_description)

def display_long_description(long_description):
    console = Console()
    markdown = Markdown(long_description)
    console.print(markdown)
    
    
