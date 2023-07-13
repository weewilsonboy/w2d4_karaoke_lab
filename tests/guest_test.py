import unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Jim",6,"Playing God")
        self.song1 = Song("Hallowed Be Thy Name")
        self.guest2 = Guest("Bruce Dickinson", 120, "Hallowed Be Thy Name")
        self.room = Room("Room 1", 4,6)
        self.room.add_song(self.song1)

    def test_guest_constructor(self):
        self.assertEqual("Jim",self.guest.name)

    def test_fav_song(self):
        expected = "Woo"
        actual = self.guest2.find_fav(self.room)


        self.assertEqual(expected, actual)