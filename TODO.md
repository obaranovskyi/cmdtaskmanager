### Investigations
- Investigate argparse
    - https://docs.python.org/3/library/argparse.html
- there is one great answer which show the straightforward example:
    - https://stackoverflow.com/questions/20063/whats-the-best-way-to-parse-command-line-arguments
- subparsers is what I'm looking for:
    - https://stackoverflow.com/questions/64084200/how-to-parse-one-group-out-of-the-two-groups-of-command-line-arguments-using-arg
- exclusive groups:
    - https://stackoverflow.com/questions/11154946/require-either-of-two-arguments-using-argparse
- get id after insert discussion:
    - https://stackoverflow.com/questions/1316952/sqlalchemy-flush-and-get-inserted-id

## TODO:
    - add task comments feature
    - consider adding raw tasks (for piping)
    - status for the project should be started when some of the project task started
    - consider adding create status feature (to me it looks more to not add it)
    - add ignorecase checks to unique updates and creates

## Features
- [1] Add comment feature
- [5] Consider adding full path handling for the long description

## Refactoring
- Consider using single exception as all you need is `e.message`


## Important: investigate this approach: 
- https://stackoverflow.com/questions/41270319/how-do-i-query-an-association-table-in-sqlalchemy
- need to revisit, and understand it more
- c - stands for the column
