import datetime
from .update_task import update_task as update_task_handler
from ..shared.parser import subparsers


def update_task_subparser():
    update_task = subparsers.add_parser('update-task', help='Update task.')
    update_task.add_argument('id', type=str, help='Task id.')
    update_task.add_argument('-t', '--title', type=str, required=False,
                             metavar='', help="Task title.")
    update_task.add_argument('-p', '--priority', type=int, required=False,
                             metavar='[0-10]', choices=range(0, 11), 
                             help="Update the priority from 0 to 10. The default is 5.")
    update_task.add_argument('-d', '--description', type=str, required=False,
                             metavar='', help='Task description.')
    update_task.add_argument('-ld', '--long-description', type=str, required=False,
                             metavar='',
                             help='The task description might be taken from the markdown file you specify.')
    update_task.add_argument('-fd', '--finish-date',
                             metavar='', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'),
                             required=False,
                             help='Date till when the task has to be finished. ' +
                                  'A format looks like this "Year-Month-Day". ' +
                                  'Here is an example: 2022-10-11')
    # status exclusive group
    update_task_status = update_task.add_mutually_exclusive_group(required=False)
    update_task_status.add_argument('-sn', '--status-name', type=str, required=False,
                                       metavar='',  help='Status name.')
    update_task_status.add_argument('-si', '--status-id', type=int, required=False,
                                       metavar='', help='Status id.')
    # tag exclusive group
    update_task_tags = update_task.add_mutually_exclusive_group(required=False)
    update_task_tags.add_argument('-tns', '--tag-names', type=str, required=False,
                                       metavar='', nargs='*', 
                                       help='Related tag names.')
    update_task_tags.add_argument('-tis', '--tag-ids', type=str, required=False,
                                       metavar='', nargs='*', 
                                       help='Related tag ids.')
    # project exclusive group
    update_task_project = update_task.add_mutually_exclusive_group(required=False)
    update_task_project.add_argument('-pn', '--project-name', type=str, required=False,
                                     metavar='', help='Related project name.')
    update_task_project.add_argument('-pi', '--project-id', type=int, required=False,
                                     metavar='', help='Related project id.')
    update_task.set_defaults(func=update_task_handler)

