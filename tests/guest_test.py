import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Jim",6)

    def test_guest_constructor(self):
        self.assertEqual("Jim",self.guest.name)