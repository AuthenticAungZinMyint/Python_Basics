#password
#demo if statement
print('Welcome to System Security Inc.')
print('-- where security is our middle name\n')
password = input('Enter your password:')
if password == 'aung#1997':
    print('Access Granted')
else:
    print('invalid password')
    password = input('Fill your ID:')
    if password == '12345':
        print('Authentic User')
    else:
        print('You are invalid user')
    input('\n\nPress the enter key to exit.')
