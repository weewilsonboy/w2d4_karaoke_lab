class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.CAPACITY = capacity
        self._guests = []
        self._songs = []

    