import datetime

def handle_add_task(args):
    print('in handle add task')
    print(args)


def add_task_subparser(subparsers):
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
                          help='The task description might be taken from the file you specify.')
    add_task.add_argument('-pn', '--project-name', type=str, required=False,
                          metavar='',
                          help='Related project.')
    add_task.add_argument('-ts', '--tags', type=str, required=False,
                          metavar='', nargs='*',
                          help='Related tags.')
    add_task.add_argument('-fd', '--finish-date',
                          metavar='',
                          type=lambda s: datetime.datetime.strptime(s, '%d-%m-%Y'),
                          required=False,
                          help='Date till when the task has to be finished. ' +
                               'A format looks like this "Year-Month-Day". ' +
                               'Here is an example: 2022-10-11')
    add_task.set_defaults(func=handle_add_task)
