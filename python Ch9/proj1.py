#Aliean Blaster
#demo obj interaction

class Player(object):
    """ A player in a shooter game. """
    def blast(self, enemy):
        print("The player blasts an enemy\n")
        enemy.die()

class Alien(object):
    """An alien in shooter game"""
    def die(self):
        print("The alien gasps and says, oh, this is it. This is the big one. \n" \
              "Yes, it's getting dark noe. Tell my 1.6 million larvae that i loved them...\n" \
              "Goodbye, cruel universe.")

#main
print("\t\tDealth of an alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\n\nPress the enter key to exit.")
