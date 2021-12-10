class Team:

  name = None
  members = set()

  def __init__(self, name):
    self.name = name
    self.members = set()

  def __eq__(self, other):
    if isinstance(other, Team):
        return self.name == other.name and self.members == other.members
    return False

  def __hash__(self):
    members_hash = 1
    for member in self.members:
      members_hash = members_hash * hash(member)
    return 37 * hash(self.name) * hash(members_hash)

  def __str__(self):
    return f'{self.name}'
