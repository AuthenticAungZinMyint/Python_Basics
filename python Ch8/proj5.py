#Private Critter
#demo private variable and method

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print("A new critter has been born")
        self.name = name #public attribute
        self.__mood = mood #privatevattribute

    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")

    def __private_method(self):
        print("\nThis is a private method")


    def public_method(self):
        print("This is a public method.")
        self.__private_method()
#main
crit = Critter(name = "Poochie", mood = "happy")
crit.talk()
crit.public_method()

input("\nPress the enter key to exit")
