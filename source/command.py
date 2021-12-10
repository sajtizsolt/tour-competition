class Command:

  def __init__(self, raw_command):
    command_parts = raw_command.split(' ')
    self.team_name = command_parts[0]
    self.member_name = command_parts[1]

  def __eq__(self, other):
    if isinstance(other, Command):
        return self.team_name == other.team_name and self.member_name == other.member_name
    return False

  def __hash__(self):
    return 37 * hash(self.team_name) * hash(self.member_name)

  def __str__(self):
    return f'{self.team_name} {self.member_name}'
