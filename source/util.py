from messages import Messages

import sys

def print_help_and_exit(message):
  print(message)
  print(Messages.HELP)
  sys.exit()
