class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.CAPACITY = capacity
        self._guests = []
        self._songs = []

    def get_guest(self, number):
        return self._guests[number]
    
    def add_guest(self, guest):
        if len(self._guests) < self.CAPACITY:
            self._guests.append(guest)
            return True
        else:
            return False
        
    def add_song(self, song):
        self._songs.append(song)

    def get_song(self, song):
        return self._songs[song]