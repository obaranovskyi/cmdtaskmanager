[INVESTIGATION] Investigate argparse
    https://docs.python.org/3/library/argparse.html
    there is one great answer which show the straightforward example:
        https://stackoverflow.com/questions/20063/whats-the-best-way-to-parse-command-line-arguments
    subparsers is what I'm looking for:
        https://stackoverflow.com/questions/64084200/how-to-parse-one-group-out-of-the-two-groups-of-command-line-arguments-using-arg
    exclusive groups:
        https://stackoverflow.com/questions/11154946/require-either-of-two-arguments-using-argparse

[FEATURES] Add task model. It should have the following properties:
    `task_id`
    `title`
    `description`
    `long_description`
    `priority 1..10`
    `status not started | in progress | done`
    `date created`
    `due date`
