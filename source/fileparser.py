from commandparser import CommandParser

class FileParser:

  command_parser = CommandParser()

  def verify_file(self, filename):
    file = open(filename, 'r')
    file_content = file.read()
    file_lines = file_content.split('\n')
    for line in file_lines:
      if len(line) > 0:
        self.command_parser.verify_command(line)

  def get_commands(self, filename):
    file = open(filename, 'r')
    file_content = file.read()
    file_lines = file_content.split('\n')
    selected_lines = []
    for line in file_lines:
      if len(line) > 0:
        selected_lines.append(line)
    return selected_lines
