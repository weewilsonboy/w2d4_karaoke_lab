import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Jim")

    def test_guest_constructor(self):
        self.assertEqual("Jim",self.guest.name)