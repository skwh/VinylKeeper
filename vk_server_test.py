import unittest

from vk_server import VKServer


class VKServerTest(unittest.TestCase):
    # TODO: Fix test_good_server_create
    @unittest.skip("test_good_server_create: Permission denied on socket open")
    def test_good_server_create(self):
        port_number = 80
        database_path = 'vinyl_keeper.db'
        # TODO: Better mocking of good server
        vkserver = VKServer(port_number, database_path)
        self.assertEqual(vkserver.status(), 'Ready')

    def test_bad_port_number(self):
        bad_port_number = 'string'
        with self.assertRaises(TypeError):
            VKServer(bad_port_number, 'vinyl_keeper.db')

            # TODO: Tests for other server methods and functionality
