#no vowers
#Demo creating new string with for loop
message = input('enter a message:')
new_message = ''
VOWELS = 'aeiou'
print()
for letter in message:
    if letter.lower()not in VOWELS:
        new_message += letter
        print('A new string has been created:', new_message)
print('\nIf your message without vowels is:', new_message)
input('\n\nPress the enter key to exit')    
