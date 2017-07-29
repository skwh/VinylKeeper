import unittest

from vk_database import VKDatabase, DatabaseError


class VKDatabaseTest(unittest.TestCase):
    def test_bad_database_path(self):
        bad_path = 'oogly_boogly'
        with self.assertRaises(DatabaseError):
            VKDatabase(bad_path)

    def test_empty_database(self):
        empty_database_path = 'fake_database.db'
        with self.assertRaises(DatabaseError):
            VKDatabase(empty_database_path)

    def test_good_database(self):
        # TODO: Better mocking of database
        good_db_path = 'vinyl_keeper.db'
        good_db = VKDatabase(good_db_path)
        self.assertIsInstance(good_db, VKDatabase)

        # TODO: Tests for database retrieval methods
