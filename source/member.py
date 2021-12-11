class Member:

  def __init__(self, name):
    self.name = name
    self.is_stolen = False

  def __eq__(self, other):
    if isinstance(other, Member):
        return self.name == other.name and self.is_stolen == other.is_stolen
    return False

  def __hash__(self):
    return hash(id(self))

  def __str__(self):
    if self.is_stolen:
      return f'{self.name} (stolen)'
    return f'{self.name}'
