# construct critter
# demo constructors
class Critter(object):
    """A virtual pet"""
    def _init_(self):
        print("A new critter has been born!")

    def talk(self):
        print("\nHi. I am instance of class Critter")

#main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nPress the enter key to exit.")
