from member import Member
from team import Team

class Database:

  def __init__(self):
    self.deleted_team_names = set()
    self.teams = set()
    self.members = set()

  def execute_command(self, command):
    print(f'\nExecuting command: {command}')
    team_name = command.team_name
    member_name = command.member_name
    if self.is_deleted_team(team_name):
      print(f'> Deleted teams can not be modified or re-created!')
      return
    is_new_team = self.is_new_team(team_name)
    is_new_member = self.is_new_member(member_name)
    if is_new_team and is_new_member:
      self.create_team_with_new_member(team_name, member_name)
    elif is_new_team and not is_new_member:
      print(f'> Can not construct team only from stolen members!')
      return
    elif not is_new_team and is_new_member:
      self.add_new_member_to_existing_team(team_name, member_name)
    elif not is_new_team and not is_new_member:
      if self.is_member_of_team(team_name, member_name):
        self.delete_member_from_team(team_name, member_name)
      else:
        self.steal_member_from_another_team(team_name, member_name)

  def is_deleted_team(self, team_name):
    for deleted_team_name in self.deleted_team_names:
      if deleted_team_name == team_name:
        return True
    return False

  def is_new_team(self, team_name):
    for team in self.teams:
      if team.name == team_name:
        return False
    return True

  def is_new_member(self, member_name):
    for member in self.members:
      if member.name == member_name:
        return False
    return True

  def get_existing_team(self, team_name):
    for team in self.teams:
      if team.name == team_name:
        return team

  def get_existing_member(self, member_name):
    for member in self.members:
      if member.name == member_name:
        return member

  def delete_team(self, team_name):
    team = self.get_existing_team(team_name)
    self.teams.remove(team)
    self.deleted_team_names.add(team_name)
    print(f'> {team_name} has ran out of members.')

  def is_member_of_team(self, team_name, member_name):
    team = self.get_existing_team(team_name)
    return team.contains_member(member_name)

  def get_team_of_member(self, member_name):
    for team in self.teams:
      if team.contains_member(member_name):
        return team

  def create_team_with_new_member(self, team_name, member_name):
    new_member = Member(member_name)
    self.members.add(new_member)
    new_team = Team(team_name)
    new_team.members.add(new_member)
    self.teams.add(new_team)
    print(f'> {team_name} is a new team.')
    print(f'> {member_name} is a new member of {team_name}.')

  def add_new_member_to_existing_team(self, team_name, member_name):
    new_member = Member(member_name)
    self.members.add(new_member)
    existing_team = self.get_existing_team(team_name)
    existing_team.members.add(new_member)
    print(f'> {team_name} is an existing team.')
    print(f'> {member_name} is a new member of {team_name}.')

  def delete_member_from_team(self, team_name, member_name):
    existing_member = self.get_existing_member(member_name)
    existing_team = self.get_existing_team(team_name)
    existing_team.members.remove(existing_member)
    print(f'> {team_name} is an existing team.')
    print(f'> {member_name} is no longer a member of {team_name}.')
    if len(existing_team.members) == 0:
      self.delete_team(existing_team.name)

  def steal_member_from_another_team(self, team_name, member_name):
    existing_member = self.get_existing_member(member_name)
    previous_team = self.get_team_of_member(member_name)
    next_team = self.get_existing_team(team_name)
    previous_team.members.remove(existing_member)
    existing_member.is_stolen = True
    next_team.members.add(existing_member)
    print(f'> {team_name} is an existing team.')
    print(f'> {member_name} is no longer a member of {previous_team.name}.')
    print(f'> {member_name} is now a member of {next_team.name}.')
    if len(previous_team.members) == 0:
      self.delete_team(previous_team.name)

  def print(self):
    print(f'\nTeams')
    for team in self.teams:
      print(f'  + {team.name}')
      for member in team.members:
        print(f'    + {member}')
    print(f'\nDeleted teams')
    for team_name in self.deleted_team_names:
      print(f'  - {team_name}')
    print()
