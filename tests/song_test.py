import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Hallowed Be Thy Name")

    def test_song_constructors(self):
        self.assertEqual("Hallowed Be Thy Name", self.song.name)