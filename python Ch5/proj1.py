Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #hero iventory 3.0
>>> #demo lists
>>> #create list with some items and display with a for loop
>>> iventory = ["sword", "armor", "shield", "healing potion"]
>>> print("your item:")
your item:
>>> for item in iventory:
	print(item)

sword
armor
shield
healing potion
>>> input("\nPress the enter key to continue")

Press the enter key to continue
''
>>> #get the length of list
>>> print("you have", len(iventory), "items in your pocession.")
you have 4 items in your pocession.
>>> input("\nPress the enter key to continue")

Press the enter key to continue
''
>>> #test for membership with tuples.
>>> if "healing potion" in iventory:
	print("You will have to fight another day.")

You will have to fight another day.
>>> #display one item through index
>>> index = int(input("\nEnter the index number for an item in iventory:"))

Enter the index number for an item in iventory:3
>>> print("At index", index, "is", iventory[index])
At index 3 is healing potion
>>> #display a slice
>>> start = int(input("\nEnter the index number to begin slice:"))

Enter the index number to begin slice:0
>>> finish = int(input("Enter the index number to end the slice:"))
Enter the index number to end the slice:2
>>> print("inentory[", start, ":", finish, "] is", end="")
inentory[ 0 : 2 ] is
>>> print(iventory[start:finish])
['sword', 'armor']
>>> input("\nPress the enter key to continue")

Press the enter key to continue
''
>>> #concatenate two lists
>>> chest = ["gold", "gems"]
>>> print("you find a chest which contains:")
you find a chest which contains:
>>> print(chest)
['gold', 'gems']
>>> print("You add the content of the chest to your iventory.")
You add the content of the chest to your iventory.
>>> iventory += chest
>>> print("your iventory is now:")
your iventory is now:
>>> print(iventory)
['sword', 'armor', 'shield', 'healing potion', 'gold', 'gems']
>>> input("\nPress the enter key to continue")

Press the enter key to continue
''
>>> #assign by index
>>> print("You trade your sword for a crossbow.")
You trade your sword for a crossbow.
>>> iventory[0] = "crossbow"
>>> print(iventory)
['crossbow', 'armor', 'shield', 'healing potion', 'gold', 'gems']
>>> iventory[6] = "Diamond"
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    iventory[6] = "Diamond"
IndexError: list assignment index out of range
>>> iventory[5] = "diamond"
>>> print(iventory)
['crossbow', 'armor', 'shield', 'healing potion', 'gold', 'diamond']
>>> input("\nPress the enter key to continue")

Press the enter key to continue
''
>>> #assign by slice
>>> print("You use your gold and gems to buy an orb of future telling.")
You use your gold and gems to buy an orb of future telling.
>>> iventory[4:6] = ["orb of future telling"]
>>> print("Your iventory is now:")
Your iventory is now:
>>> print(iventory)
['crossbow', 'armor', 'shield', 'healing potion', 'orb of future telling']
>>> input("\nPress the enter key to continue.")

Press the enter key to continue.
''
>>> #Delete an element
>>> print("In a great battle, your shield is destroyed.")
In a great battle, your shield is destroyed.
>>> del iventory[2]
>>> print(iventory)del iventory[2]
SyntaxError: invalid syntax
>>> del iventory[2]
>>> print("your iventory is now:")
your iventory is now:
>>> print(iventory)
['crossbow', 'armor', 'orb of future telling']
>>> input("\nPress the enter key to continue")

Press the enter key to continue
''
>>> #delete a slice
>>> print("Your crossbow and armor are stolen by thieves")
Your crossbow and armor are stolen by thieves
>>> del iventory[:2]
>>> print("your iventory is now:)
      
SyntaxError: EOL while scanning string literal
>>> print("your iventory is now")
your iventory is now
>>> print(iventory)
['orb of future telling']
>>> input("\nPress the enter key to exit")

Press the enter key to exit
''
>>> 