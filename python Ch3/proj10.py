#Exclusive network
#Demo logical operator and compound conditions
print('\t\t Friendship Network')
print('\t\t\tMember only\n')
security = 0
username = ''
while not username:
    username = input('Username:')
password = ''
while not password:
    password = input('password:')
if username == 'Ei' and password =='secret':
    print('Hi!Ei')
    security = 5
elif username == 'Min Chit' and password == 'beauty':
    print('Hi!Min')
    security = 3
elif username == 'Lynn Thant' and password == 'bignose':
    print('Hi!Lynn')
    security = 3
elif username =='Ye Yint' and password =='tally':
    print('Hi!Ye')
    security = 3
elif username == 'Aye' and password == 'shorty':
    print('Hi!Aye')
    security = 1
else:
    print('Log in failed. You are not eligible\n')
input('\n\nPress the enter key to exit')
