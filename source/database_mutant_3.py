from command import Command
from database import Database
from member import Member
from team import Team

class DatabaseMutant03(Database):

  def steal_member_from_another_team(self, team_name, member_name):
    existing_member = self.get_existing_member(member_name)
    previous_team = self.get_team_of_member(member_name)
    next_team = self.get_existing_team(team_name)
    if len(next_team.members) != 2:
      print(f'> A team can only steal members, if it makes it complete!')
      return
    previous_team.members.remove(existing_member)
    existing_member.is_stolen = True
    next_team.members.add(existing_member)
    print(f'> {team_name} is an existing team.')
    print(f'> {member_name} is no longer a member of {previous_team.name}.')
    print(f'> {member_name} is now a member of {next_team.name}.')
    if len(previous_team.members) == 0:
      self.delete_team(previous_team.name)

if __name__ == '__main__':
  m1 = Member('M1')
  m1.is_stolen = True
  m2 = Member('M2')
  m3 = Member('M3')
  m4 = Member('M4')
  t1 = Team('T1')
  t1.members.add(m1)
  t1.members.add(m2)
  t2 = Team('T2')
  t2.members.add(m3)
  t2.members.add(m4)
  database = DatabaseMutant03()
  database.teams.add(t1)
  database.teams.add(t2)
  database.members.add(m1)
  database.members.add(m2)
  database.members.add(m3)
  database.members.add(m4)

  database.execute_command(Command('T2 M2'))

  database.print()
