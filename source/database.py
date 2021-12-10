import re
from member import Member
from team import Team

class Database:

  def __init__(self):
    self.deleted_teams = set()
    self.teams = set()
    self.members = set()

  def execute_command(self, command):
    print(f'\nExecuting command: {command}')
    if self.is_team_deleted(command.team_name):
      print(f'> Deleted teams can not modified!')
      return
    if self.is_new_team(command.team_name):
      self.create_team(command.team_name, command.member_names)
    else:
      self.modify_team(command.team_name, command.member_names)

  def create_team(self, team_name, member_names):
    print(f'> {team_name} is a new team.')
    if len(member_names) > 3:
      print(f'> A new team can contain at most 3 members!')
      return
    if not self.does_list_contain_new_member_name(member_names):
      print(f'> Can not construct team only from stolen members!')
      return
    new_team = Team(team_name)
    for member_name in member_names:
      if self.is_member_name_new(member_name):
        member = Member(member_name)
        self.members.add(member)
        new_team.members.add(member)
        print(f'> {member_name} is a new member.')
      else:
        member = self.get_member(member_name)
        old_team = self.get_team_of_member(member)
        old_team.members.remove(member)
        member.is_stolen = True
        new_team.add(member)
        print(f'> Stealing {member_name} from {old_team.name}')
    self.teams.add(new_team)

  def modify_team(self, team_name, member_names):
    print(f'> {team_name} is an existing team.')
    # TODO: Check if stolen to deleted ratio is correct
    # TODO: Check if not everyone is stolen
    # TODO: Check if team number at the end correct
    team = self.get_team(team_name)
    for member_name in member_names:
      if self.is_member_name_new(member_name):
        if len(team.members) > 2:
          print(f'> A team can contain at most 3 members!')
          return
        member = Member(member_name)
        self.members.add(member)
        new_team.members.add(member)
        print(f'> {member_name} is a new member.')
      else:
        member = self.get_member(member_name)
        old_team = self.get_team_of_member(member)
        old_team.members.remove(member)
        member.is_stolen = True
        new_team.add(member)
        print(f'> Stealing {member_name} from {old_team.name}')

  def get_team(self, team_name):
    for team in self.teams:
      if team.name == team_name:
        return team

  def get_member(self, member_name):
    for member in self.members:
      if member.name == member_name:
        return member

  def is_team_deleted(self, team_name):
    return Team(team_name) in self.deleted_teams

  def is_new_team(self, team_name):
    for team in self.teams:
      if team.name == team_name:
        return False
    return True

  def is_member_name_new(self, member_name):
    for member in self.members:
      if member.name == member_name:
          return False
    return True

  def get_team_of_member(self, member_name):
    for team in self.teams:
      if team.contains_member(member_name):
        return team

  def does_list_contain_new_member_name(self, member_names):
    for name in member_names:
      if self.is_member_name_new(name):
        return True
    return False

  def print(self):
    print(f'\nTeams')
    for team in self.teams:
      print(f'  + {team.name}')
      for member in team.members:
        print(f'    + {member.name}')
    print(f'\nDeleted teams\n')
    for team in self.deleted_teams:
      print(f'  - {team.name}')
