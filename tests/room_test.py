import unittest

from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1", 4)

    def test_room_construct(self):
        self.assertEqual("Room 1", self.room.name)