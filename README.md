# tour-competition

## Task description

A tour competition application can handle registered teams as follows:

- During the registration process a unique team name together with globally unique team members can be entered. A team has at least one and at most three members. The registration is activated when ‘Add team’ is pressed.
- After entering an existing team name, missing team members can be added and existing team members can be deleted or modified.
- Members of incomplete teams can be ‘stolen’, i.e., they can be added to another team during registration or modification, only if the 'thief' team is complete.
- It is not allowed to construct a team only from 'stolen' members.
- If all the team members have been 'stolen' from a team, it’s deleted automatically, and no new team can be registered with the deleted team’s name.
- Stolen member cannot be modified only deleted. Stolen members can be further stolen from incomplete teams.

### Additional information

- The code should be written in Python.
- There is no need for a real database, it can be "mocked".
- The code should be clean.
- There is no need for GUI.

## How to use

To try the application, run one of the following examples:

```shell
$ py source/main.py "T1 M1" "T1 M2" "T1 M3" "T2 M4" "T2 M5" "T3 M6" "T2 M6"
```

or

```shell
$ py source/main.py data/test_commands
```

### How to run tests

To run the tests, run the following command:

```shell
$ py source/database_test.py
```

## Mutants

There are some mutants of the `Database` class, which shows that small programming mistakes can lead to huge problems.

### 1

A developer can forget about the maximum number of members in a team, and the lack of this check can lead to teams with more than 3 members.

### 2

A developer can forget about that when the user wants to delete a team member, we have to check if the remaining members are stolen, or not, because a deletion can lead to a team consisting of only stolen members.

### 3

A developer can forget about that when a team is stealing a member from another team, we have to check if the remaining members of the previous team should not be all stolen.

### 4

A developer can forget about that when a team is stealing a member from another team, the process can only be successful if the stealing will make the thief team complete (consisting of 3 members).

### 5

A developer can commit a simple typo in the code, for example write `1` insted of `0`, which can lead to not deleting the empty team from the database.
