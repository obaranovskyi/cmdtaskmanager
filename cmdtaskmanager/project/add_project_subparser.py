import datetime
from .add_project import add_project as add_project_handler
from ..shared.parser import subparsers


def add_project_subparser():
    add_project = subparsers.add_parser('add-project', help='Add project.')
    add_project.add_argument('-n', '--name', type=str,
                          metavar='',
                          help='Project name.')
    add_project.add_argument('-d', '--description', type=str, required=False,
                          metavar='',
                          help='Project description.')
    add_project.add_argument('-fd', '--finish-date',
                          metavar='',
                          type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'),
                          required=False,
                          help='Date till when the project has to be finished. ' +
                               'A format looks like this "Year-Month-Day". ' +
                               'Here is an example: 2022-10-11')
    add_project.set_defaults(func=add_project_handler)
