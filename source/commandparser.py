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
    member_names = set()
    self.verify_team_name(command_parts[0])
    self.verify_member_names(command_parts[1 : command_parts_length])

  def verify_team_name(self, team_name):
    if not re.fullmatch(self.REGEX_TEAM, team_name):
      print_help_and_exit(Messages.INVALID_TEAM_NAME)

  def verify_member_names(self, member_names):
    verified_names = set()
    for name in member_names:
      if not re.fullmatch(self.REGEX_PERSON,name):
        print_help_and_exit(Messages.INVALID_MEMBER_NAME)
      if name in verified_names:
        print_help_and_exit(Messages.MEMBER_NAME_DUPLICATE)
      verified_names.add(name)
