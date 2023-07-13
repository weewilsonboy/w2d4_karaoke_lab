import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Room 1", 4)
        self.song1 = Song("Hallowed Be Thy Name")
        self.guest1 = Guest("Jim")
        self.song2 = Song("Dream On")
        self.guest2 = Guest("Bruce Dickinson")


    def test_room_construct(self):
        self.assertEqual("Room 1", self.room.name)

    def test_room_add_guests(self):
        self.room.add_guest(self.guest1)
        expected = self.guest1.name
        actual = self.room.get_guest(0)
        self.assertEqual(expected, actual.name)

    def test_add_song(self):
        self.room.add_song(self.song1)
        expected = self.song1.name
        actual = self.room.get_song(0)
        actual = actual.name
        self.assertEqual(expected, actual)