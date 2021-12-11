from command import Command
from database import Database
from member import Member
from team import Team

class DatabaseMutant01(Database):

  def add_new_member_to_existing_team(self, team_name, member_name):
    existing_team = self.get_existing_team(team_name)
    new_member = Member(member_name)
    self.members.add(new_member)
    existing_team.members.add(new_member)
    print(f'> {team_name} is an existing team.')
    print(f'> {member_name} is a new member of {team_name}.')

if __name__ == '__main__':
  m1 = Member('M1')
  m2 = Member('M2')
  m3 = Member('M3')
  t1 = Team('T1')
  t1.members.add(m1)
  t1.members.add(m2)
  t1.members.add(m3)
  database = DatabaseMutant01()
  database.teams.add(t1)
  database.members.add(m1)
  database.members.add(m2)
  database.members.add(m3)

  database.execute_command(Command('T1 M4'))

  database.print()
