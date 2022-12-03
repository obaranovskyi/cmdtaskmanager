def handle_remove_task(args):
    print('in handle remove task')
    print(args)

def remove_task_subparser(subparsers):
    add_task = subparsers.add_parser('remove-task', help='Remove task.')
    add_task.add_argument('task_id', type=int, help='Task id.')
    add_task.set_defaults(func=handle_remove_task)
