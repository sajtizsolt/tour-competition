from command import Command
from database import Database
from member import Member
from team import Team

class DatabaseMutant02(Database):

  def delete_member_from_team(self, team_name, member_name):
    existing_member = self.get_existing_member(member_name)
    existing_team = self.get_existing_team(team_name)
    existing_team.members.remove(existing_member)
    self.members.remove(existing_member)
    print(f'> {team_name} is an existing team.')
    print(f'> {member_name} is no longer a member of {team_name}.')
    if len(existing_team.members) == 0:
      self.delete_team(existing_team.name)

if __name__ == '__main__':
  m1 = Member('M1')
  m2 = Member('M2')
  m3 = Member('M3')
  m1.is_stolen = True
  m2.is_stolen = True
  t1 = Team('T1')
  t1.members.add(m1)
  t1.members.add(m2)
  t1.members.add(m3)
  database = DatabaseMutant02()
  database.teams.add(t1)
  database.members.add(m1)
  database.members.add(m2)
  database.members.add(m3)

  database.execute_command(Command('T1 M3'))

  database.print()
