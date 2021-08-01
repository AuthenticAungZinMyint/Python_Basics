#Guess my number
import random
print('\tWelcome to Guess my number')
print('\nI am thinking of the number between 1 and 100')
print('Try to guess it in a few attempts as possible.\n')
the_number = random.randint(1,100)
guess = int(input('Take a guess:'))
tries = 1
while guess != the_number:
    if guess > the_number:
        print('Lower....')
    else:
        print('Higher....')
    guess = int(input('Take a guess:'))
    tries += 1
print('You guessed it! The number was', the_number)
print('And it only took you', tries, 'tries!\n')
        
