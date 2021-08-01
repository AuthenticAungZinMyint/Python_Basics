#hero inventory
#Demo tuple creation

#Create empty tuple
inventory = ()
#treat the tuple as a condition
if not inventory:
    print('You are empty handed')
input('\nPress the enter key to continue.')
#create a tuple with some items
inventory = ('sword',
             'armor',
             'shield',
             'healing potion')
#print the tuple
print('The inventory is:')
print(inventory)
#print each element in the tuple
print('\n your item is:')
for  item in inventory:
    print(item)
input('\nPress the enter key to exit')
