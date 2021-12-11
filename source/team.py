class Team:

  def __init__(self, name):
    self.name = name
    self.members = set()

  def __eq__(self, other):
    if isinstance(other, Team):
        return self.name == other.name and self.members == other.members
    return False

  def __ne__(self, other):
    return not self == other

  def __hash__(self):
    return hash(id(self))

  def __str__(self):
    members_str = ''
    for member in self.members:
      members_str += f' {member}'
    return f'{self.name}{members_str}'

  def contains_member(self, member_name):
    for member in self.members:
      if member.name == member_name:
        return True
    return False

  def is_complete(self):
    return len(self.members) == 3
