from commandparser import CommandParser
from fileparser import FileParser
from messages import Messages
from util import print_help_and_exit

import os
import sys

class ArgumentParser:

  def __init__(self):
    self.command_parser = CommandParser()
    self.file_parser = FileParser()
    self.is_file = True

  def verify_arguments(self, arguments):
    argument_count = len(arguments)
    if argument_count == 1:
       print_help_and_exit(Messages.TOO_FEW_ARGUMENTS)
    elif argument_count == 2:
      argument = arguments[argument_count - 1]
      if os.path.isfile(argument):
        self.file_parser.verify_file(argument)
      else:
        self.is_file = False
        self.command_parser.verify_command(argument)
    else:
      self.is_file = False
      for i in range(1, argument_count):
        self.command_parser.verify_command(arguments[i])

  def get_commands(self, arguments):
    if self.is_file:
      return self.file_parser.get_commands(arguments[1])
    else:
      return sys.argv[1 : len(sys.argv)]
