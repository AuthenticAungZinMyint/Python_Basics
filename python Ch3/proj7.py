#Losing Battle
#Demo  fixing infinite loop
health = 20
trolls = 0
damage = 2
while health > 0:
    trolls += 1
    health -= damage
    print ('Your hero swings and defeated an evil troll,' \
           'but takes', damage, 'damage points.\n')
    
print('Your hero fought valiantly and defeated', trolls, 'trolls')
print('but alas, your hero is no more')
input('\n\nPress the enter key to exit.')
