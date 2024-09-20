#Need:
#   jukebox: insert coin, play music, music list, etc

class Music_Disc:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Jukebox:
    def __init__(self):
        self.current_disc = None
        self.stored_income = 0

    def play(self, disc, coin):
        self.stored_income += coin
        if disc.price > coin:
            print "please pay the necessary amount."
            return coin #give money back
        else:
            self.current_disc = disc
            return 1 #indicates successful insertion of music