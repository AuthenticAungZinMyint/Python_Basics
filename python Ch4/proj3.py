#message analyzer
#demo len() fun
message = input('Enter a messsage:')
print('\nthe length of your message is:' , len(message))
print('\nthe most commom letter in your message in the english language, "e",')
if 'e' in message:
    print('is in your message.')
else:
    print('is not in your message')
input('\n\nPress the enter key to exit')
