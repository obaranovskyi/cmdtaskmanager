from .display_task_list_subparser import display_task_list_subparser
from .display_task_subparser import display_task_subparser
from .remove_task_subparser import remove_task_subparser
from .add_task_subparser import add_task_subparser
from .update_task_subparser import update_task_subparser
from .update_task_status_subparser import (reset_task_subparser, start_task_subparser,
                                           complete_task_subparser, postpone_task_subparser,
                                           remove_task_subparser as update_task_status_to_removed)

def register_task_subparsers():
    display_task_subparser()
    display_task_list_subparser()
    add_task_subparser()
    update_task_subparser()
    remove_task_subparser()
    # status updates
    reset_task_subparser()
    start_task_subparser()
    complete_task_subparser()
    postpone_task_subparser()
    update_task_status_to_removed()
