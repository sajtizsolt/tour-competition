from argumentparser import ArgumentParser
from command import Command
from database import Database

import sys

def main():
  argument_parser = ArgumentParser()
  argument_parser.verify_arguments(sys.argv)
  command_list = argument_parser.get_commands(sys.argv)
  database = Database()
  for command_str in command_list:
    database.execute_command(Command(command_str))
  database.print()

if __name__ == '__main__':
  main()
