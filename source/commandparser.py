import re

class CommandParser:

  REGEX_TEAM = re.compile("[a-zA-Z0-9_]+")
  REGEX_PERSON = re.compile("[a-zA-Z0-9_]+")

  def verify_command(self, command):
    print(command)
    command_parts = command.split(" ")
    command_parts_length = len(command_parts)
    if command_parts_length < 2 or command_parts_length > 7:
      print("TODO: Invalid command length")
    if not re.fullmatch(self.REGEX_TEAM, command_parts[0]) :
      print("TODO: Invalid team name")
    for i in range(1, command_parts_length):
      if not re.fullmatch(self.REGEX_PERSON, command_parts[i]):
        print("TODO: Invalid person name")
