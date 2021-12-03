from commandparser import CommandParser
from messages import Messages

import os
import sys

class ArgumentParser:

  is_file = None

  @staticmethod
  def print_help_and_exit(message):
    print(message)
    print(Messages.HELP)
    sys.exit()

  @staticmethod
  def verify_arguments():
    argument_count = len(sys.argv)
    if argument_count == 0:
       ArgumentParser.print_help_and_exit(Messages.TOO_FEW_ARGUMENTS)
    elif argument_count == 1:
      if not os.path.isfile(sys.argv[argument_count - 1]):
        ArgumentParser.print_help_and_exit(Messages.INVALID_FILE_PATH)

