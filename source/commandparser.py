from messages import Messages
from util import print_help_and_exit

import re

class CommandParser:

  REGEX_TEAM = re.compile("[a-zA-Z0-9_]+")
  REGEX_PERSON = re.compile("[a-zA-Z0-9_]+")

  def verify_command(self, command):
    print(command)
    command_parts = command.split(" ")
    command_parts_length = len(command_parts)
    if command_parts_length < 2:
      print_help_and_exit(Messages.TOO_SHORT_COMMAND)
    elif command_parts_length > 7:
      print_help_and_exit(Messages.TOO_LONG_COMMAND)
    if not re.fullmatch(self.REGEX_TEAM, command_parts[0]) :
      print_help_and_exit(Messages.INVALID_TEAM_NAME)
    for i in range(1, command_parts_length):
      if not re.fullmatch(self.REGEX_PERSON, command_parts[i]):
        print_help_and_exit(Messages.INVALID_MEMBER_NAME)
