class Messages:

  HELP = '''
    Usage:  python main.py { FILE | COMMAND [COMMAND ...] }

    where COMMAND is

      TEAM_NAME PERSON_NAME

    and

      TEAM_NAME can only contain A-z letters, 0-9 numbers and _ characters

    and

      PERSON_NAME can only contain A-z letters, 0-9 numbers and _ characters

    Notes:

      Files should contain exactly one command per line.

      Commands as argument should be strings, so sorround it with quotation
      marks.
  '''

  TOO_FEW_ARGUMENTS = '''
    Too few command line arguments. You must specify the file that contain the commands, or a list of commands (at least one)!
  '''

  INVALID_FILE_PATH = '''
    The specified file path is invalid. Please check if the given file exists.
  '''

  INVALID_COMMAND = '''
    The specified command is invalid. A command should contain exactly one
    team name and exactly one member name.
  '''

  INVALID_TEAM_NAME = '''
    The given team name is invalid. A team name can only contain lower and
    uppercase letters, numbers and underscore characters.
  '''

  INVALID_MEMBER_NAME = '''
    The given member name is invalid. A member name can only contain lower and uppercase letters, numbers and underscore characters.
  '''
