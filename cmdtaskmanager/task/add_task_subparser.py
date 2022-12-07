import datetime
from .add_task import add_task as add_task_handler
from ..shared.parser import subparsers


def add_task_subparser():
    add_task = subparsers.add_parser('add-task', help='Add task.')
    add_task.add_argument('title', type=str, help='Task title.')
    add_task.add_argument('-p', '--priority', type=int, required=False,
                          metavar='[0-10]', choices=range(0, 11), 
                          help="Set the priority from 0 to 10. The default is 5.",
                          default=5)
    add_task.add_argument('-d', '--description', type=str, required=False,
                          metavar='',
                          help='Task description.')
    add_task.add_argument('-ld', '--long-description', type=str, required=False,
                          metavar='',
                          help='The task description might be taken from the markdown file you specify.')
    add_task.add_argument('-fd', '--finish-date',
                          metavar='',
                          type=lambda s: datetime.datetime.strptime(s, '%d-%m-%Y'),
                          required=False,
                          help='Date till when the task has to be finished. ' +
                               'A format looks like this "Year-Month-Day". ' +
                               'Here is an example: 2022-10-11')
    # tag exclusive group
    add_task_tags = add_task.add_mutually_exclusive_group(required=False)
    add_task_tags.add_argument('-tns', '--tag-names', type=str, required=False,
                          metavar='', nargs='*', 
                          help='Related tag names.')
    add_task_tags.add_argument('-tis', '--tag-ids', type=str, required=False,
                          metavar='', nargs='*', 
                          help='Related tag ids.')
    # project exclusive group
    add_task_project = add_task.add_mutually_exclusive_group(required=False)
    add_task_project.add_argument('-pn', '--project-name', type=str, required=False,
                          metavar='',
                          help='Related project name.')
    add_task_project.add_argument('-pi', '--project-id', type=int, required=False,
                          metavar='',
                          help='Related project id.')
    add_task.set_defaults(func=add_task_handler)
