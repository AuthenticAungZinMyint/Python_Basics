#simple critter
#demo a basic class and object

class Critter(object):
    """A virtual pet"""
    def talk(self):
        print("Hi, I'm instance of class Critter.")
#main
crit = Critter()
crit.talk()
input("\nPress the enter key to exit")
