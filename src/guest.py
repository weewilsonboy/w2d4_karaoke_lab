class Guest:
    def __init__(self,name, money,fav):
        self.name=name
        self.money = money
        self.fav = fav

    def find_fav(self, room):
        if room.find_song(self.fav) == True:
            return "Woo"
        else:
            return "Boo"