class Room:
    def __init__(self, name, capacity, entry):
        self.name = name
        self.CAPACITY = capacity
        self._guests = []
        self._songs = []
        self.ENTRY_FEE = entry
        self.running_total = 0

    def get_guest(self, number):
        return self._guests[number]
    
    def add_guest(self, guest):
        if len(self._guests) < self.CAPACITY and guest.money >= self.ENTRY_FEE:
            self._guests.append(guest)
            guest.money -= self.ENTRY_FEE
            self.running_total += self.ENTRY_FEE
            return True
        else:
            return False
        
    def add_song(self, song):
        self._songs.append(song)

    def get_song(self, song):
        return self._songs[song]
    
    def find_song(self, song):
        for songs in self._songs:
            if songs.name == song:
                return True
            else:
                return False