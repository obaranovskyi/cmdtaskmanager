# cmdtaskmanager

`cmdtaskmanager` is a simple task manager. 

## Installation
```bash
curl -s https://raw.githubusercontent.com/obaranovskyi/cmdtaskmanager/main/install.sh | bash /dev/stdin
```

## Adding a project
On top of the hierarchy stands the project, where you can include tasks. 

**Note:** Tasks also might exist without a project, in case you want them to be for the general purpose.

To create a project, run the following command:
```bash
add-project 'Homework' -d 'Under this project, I do my homework.' -fd '2025-01-01'
```
`-d`, or `--description` - stands for the description  \
`-fd`, or `--finish-date` - stands for the finish date

Let's add one more:
```bash
add-project 'My Real Company' -d 'Here I keep the tasks related to my future company.'
```
This time we won't specify the finish date as there is no reason to do that in the current case.

Now we have projects, let's display them, with the following command:
```bash
display-project-list
```
![](./images/display-project-list.png)

In case you want to receive information only about some specific project run this command:

```bash
display-project 1
```
`1` is the project id, that might be found in the first column of the general project table.

![](./images/display-project.png)

To remove the project run:
```bash
remove-project 2
```

Let's update the project info:
```bash
update-project 2 -n 'My New Real Company' -d 'Here I keep the tasks related to my current company.'
```
**Note**: You need to pass only the properties which you want to update.

## Adding tasks
That is probably the most important part.

To create a task without a project just run the following command:
```bash
add-task 'Go to the store'
```
To create a task under the project:
```bash
add-task 'Clean up the room' -pi 1 -d 'No rush with this'
```
Now we have tasks, let's display them:
```bash
display-task-list
```
![](./images/display-task-list.png)

In case you want to display some specific task, run the following command:
```bash
display-task 2
```
`2` is the task id, that might be found in the first column of the general task table.

![](./images/display-task.png)

## Display tasks by search criteria
To show only project related tasks, run the following command:
```bash
display-task-list -pi 1
```
Where `1` is a project id
![](./images/search-by-project.png)

To show only tag related tasks, run:
```bash
display-task-list -tns 'important'
```
![](./images/search-by-tag.png)

**Note** It's possible to search by multiple tag ids or names.

To search by title, run:
```bash
display-task-list -t 'make a'
```

![](./images/search-by-title.png)

To search by description, run:
```bash
display-task-list -d 'no'
```

![](./images/search-by-description.png)

**Important** It is possible to combine multiple search criteria.

## Changing statuses

#### To display system available statuses:
```bash
display-status-list
```
![](./images/display-status-list.png)

#### To change the project status:
```bash
update-project 1 -si 2
```
`1` is the project id \
`2` is the status id

It's possible to update the project using the status name:
```bash
update-project 1 -sn 'In Progress'
```
![](./images/display-project-status-update.png)

Now we can see the status was changed.

#### To change the task status
It's possible to change task status in a similar manner as was changed status for the project.
```bash
update-task 1 -si 2
```
This command will update the task status to 'In Progress'.

But a more appropriate way of changing the task status is to use the changing status-specific commands.

Here is the task status changing commands:

Set task status to 'Not Started':
```bash
reset-task 1
```

Set task status to 'In Progress':
```bash
start-task 1
```

Set task status to 'Completed':
```bash
complete-task 1
```

Set task status to 'Postponed':
```bash
postpone-task 1
```

Set task status to 'Removed':
```bash
remove-task 1
```

## Adding comments
It's possible to add a comment to task:
```bash
add-comment 1 "It's better not to postpone this."
add-comment 1 "At least, I think so."
```
`1` is a task id

We can display comments in the table:
```bash
display-comment-list 1
```
`1` is a task id

![](./images/display-comment-list.png)

or we can display task details and see comments there:

![](./images/display-comments-in-a-task.png)

to remove the comment, run:
```bash
remove-comment 2
```

## Adding Tags
To add a tag run:
```bash
add-tag 'important' -d 'Something that has to be done quickly.'
add-tag 'test'
```
To display all available tags:
```bash
display-tag-list
```
![](./images/display-tag-list.png)

Adding tags to task
```bash
task-update 1 -tis 1 2
```
To check whether you've added the tags to the task, display task details:
```bash
display-task 1
```
![](./images/display-task-with-tags.png)

**Note** It's possible to add tags using names instead of ids.
```bash
update-task 1 -tns 'important' 'test'
```

There is an even more straightforward way to add tags to tasks.
When you're adding a new task, you can add tags. 
If the tag doesn't exist, it'll be automatically added:
```bash
add-task 'Make a coffee' -d 'But the last one for today.' -tns 'not important' 'later'
```
If you run `display-tag-list`, you'll see them on the list:

![](./images/display-tag-list-task-add.png)

if you run `display-task-list`, you'll see a new task with the tags you've provided:

![](./images/display-task-details-with-tags.png)


To remove tags from task, run this command:
```bash
update-task 1 -tns ''
```
To remove tag from the system:
```bash
remove-tag 2
```
**Note**: If some tasks used a tag, you would be notified to update the task first due to dependency.

![](./images/tag-notification.png)


### Dependencies

- We use [`rich`](https://rich.readthedocs.io/) to show everything nicely in the terminal.
- We use [`sqlalchemy`](https://www.sqlalchemy.org/) to store the data in the database.
- We use [`pytz`](https://pythonhosted.org/pytz/) to work with the dates.


### License

This project is licensed under the terms of the MIT license.
