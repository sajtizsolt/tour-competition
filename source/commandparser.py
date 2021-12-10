from messages import Messages
from util import print_help_and_exit

import re

class CommandParser:

  def __init__(self):
    self.REGEX_TEAM = re.compile("[a-zA-Z0-9_]+")
    self.REGEX_PERSON = re.compile("[a-zA-Z0-9_]+")

  def verify_command(self, command):
    command_parts = command.split(" ")
    if len(command_parts) != 2:
      print_help_and_exit(Messages.INVALID_COMMAND)
    self.verify_team_name(command_parts[0])
    self.verify_member_name(command_parts[1])

  def verify_team_name(self, team_name):
    if not re.fullmatch(self.REGEX_TEAM, team_name):
      print_help_and_exit(Messages.INVALID_TEAM_NAME)

  def verify_member_name(self, member_name):
    if not re.fullmatch(self.REGEX_PERSON, member_name):
      print_help_and_exit(Messages.INVALID_MEMBER_NAME)
