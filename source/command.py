class Command:

  team_name = None
  member_names = set()

  def __init__(self, raw_command):
    command_parts = raw_command.split(' ')
    self.team_name = command_parts[0]
    self.member_names = set()
    for name in command_parts[1 : len(command_parts)]:
      self.member_names.add(name)

  def __eq__(self, other):
    if isinstance(other, Command):
        return self.team_name == other.team_name and self.member_names == other.member_names
    return False

  def __hash__(self):
    members_hash = 1
    for member in self.member_names:
      members_hash = members_hash * hash(member)
    return 37 * hash(self.team_name) * hash(self.is_stolen)

  def __str__(self):
    members = ''
    for name in self.member_names:
      members += f' {name}'
    return f'{self.team_name}{members}'
