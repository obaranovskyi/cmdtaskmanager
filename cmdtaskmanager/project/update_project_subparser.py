import datetime
from .update_project import update_project as update_project_handler
from ..shared.parser import subparsers


def update_project_subparser():
    update_project = subparsers.add_parser('update-project', help='Update project.')
    update_project.add_argument('id', type=str, help='Project id.')
    update_project.add_argument('-n', '--name', type=str,
                          metavar='', required=False, help='Project name.')
    update_project.add_argument('-d', '--description', type=str, 
                          metavar='', required=False, help='Project description.')
    update_project.add_argument('-fd', '--finish-date',
                          metavar='', 
                          type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'),
                          required=False,
                          help='Date till when the project has to be finished. ' +
                               'A format looks like this "Year-Month-Day". ' +
                               'Here is an example: 2022-10-11')
    # status exclusive group
    update_project_status = update_project.add_mutually_exclusive_group(required=False)
    update_project_status.add_argument('-sn', '--status-name', type=str, required=False,
                                       metavar='',  help='Status name.')
    update_project_status.add_argument('-si', '--status-id', type=int, required=False,
                                       metavar='', help='Status id.')
    update_project.set_defaults(func=update_project_handler)
