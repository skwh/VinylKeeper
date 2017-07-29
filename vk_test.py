import unittest

import vk


class VKTest(unittest.TestCase):
    def test_extract_args(self):
        """Test key, value extract from sys.argv."""
        argv = ["-port=3000", "-host=localhost", "-prefix=ted"]
        expected_args = [("port", "3000"), ("host", "localhost"), ("prefix", "ted")]
        result_args = vk.extract_args(argv)
        self.assertEqual(result_args, expected_args)

    def test_get_server_args(self):
        """Test port, db name extract."""
        args = [("port", "3000"), ("testKey", "testValue")]
        expected_port, expected_db = ("3000", "database.db")
        result_port, result_db = vk.get_server_args(args)
        self.assertTupleEqual((result_port, result_db), (expected_port, expected_db))
