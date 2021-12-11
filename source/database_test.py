from command import Command
from database import Database
from member import Member
from team import Team

import unittest

class DatabaseTest(unittest.TestCase):

  # def test_create_team_with_new_member(self):
  #   database = Database()
  #   database.execute_command(Command('T1 M1'))
  #   self.assertEqual(1, len(database.teams))
  #   self.assertEqual(1, len(database.members))
  #   self.assertEqual(1, len(database.get_existing_team('T1').members))

  # def test_add_new_member_to_existing_team(self):
  #   database = Database()
  #   database.execute_command(Command('T1 M1'))
  #   database.execute_command(Command('T1 M2'))
  #   self.assertEqual(1, len(database.teams))
  #   self.assertEqual(2, len(database.members))
  #   self.assertEqual(2, len(database.get_existing_team('T1').members))

  # def test_delete_member_from_team(self):
  #   database = Database()
  #   database.execute_command(Command('T1 M1'))
  #   database.execute_command(Command('T1 M2'))
  #   database.execute_command(Command('T1 M1'))
  #   self.assertEqual(1, len(database.teams))
  #   self.assertEqual(1, len(database.members))
  #   self.assertEqual(1, len(database.get_existing_team('T1').members))
  #   database.execute_command(Command('T1 M2'))
  #   self.assertEqual(0, len(database.teams))
  #   self.assertEqual(0, len(database.members))
  #   self.assertEqual(1, len(database.deleted_team_names))

  # def test_steal_member_from_another_team(self):
  #   database = Database()
  #   database.execute_command(Command('T1 M1'))
  #   database.execute_command(Command('T1 M2'))
  #   database.execute_command(Command('T2 M3'))
  #   database.execute_command(Command('T1 M3'))
  #   self.assertEqual(1, len(database.teams))
  #   self.assertEqual(3, len(database.members))
  #   self.assertEqual(3, len(database.get_existing_team('T1').members))
  #   self.assertEqual(1, len(database.deleted_team_names))

  def test_steal_member_from_another_team(self):
    m1 = Member('M1')
    m2 = Member('M2')
    m3 = Member('M3')
    t1 = Team('T1')
    t1.members.add(m1)
    t1.members.add(m2)
    t2 = Team('T2')
    t2.members.add(m3)
    database = Database()
    database.teams.add(t1)
    database.teams.add(t2)
    database.members.add(m1)
    database.members.add(m2)
    database.members.add(m3)

    database.execute_command(Command('T1 M3'))

    self.assertEqual(1, len(database.teams))
    self.assertEqual(3, len(database.members))
    self.assertEqual(3, len(database.get_existing_team('T1').members))
    self.assertEqual(1, len(database.deleted_team_names))
    self.assertTrue(m3.is_stolen)



if __name__ == '__main__':
  unittest.main()
