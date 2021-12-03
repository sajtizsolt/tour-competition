from commandparser import CommandParser
from messages import Messages
from util import print_help_and_exit

import os

class ArgumentParser:

  command_parser = CommandParser()
  is_file = True

  def verify_arguments(self, arguments):
    argument_count = len(arguments)
    if argument_count == 1:
       print_help_and_exit(Messages.TOO_FEW_ARGUMENTS)
    elif argument_count == 2:
      argument = arguments[argument_count - 1]
      if os.path.isfile(argument):
        print("TODO: Verify file")
      else:
        is_file = False
        self.command_parser.verify_command(argument)
    else:
      is_file = False
      for i in range(1, argument_count):
        self.command_parser.verify_command(arguments[i])
