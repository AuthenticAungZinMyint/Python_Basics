print(
    '''
                Trust Fund Buddy
     Totals your monthly spending so that your trust fund does not run out
     (and you are forced to get a real job).
     Please enter the requested, monthly costs. Since you are rich, ignore pennies and use only dollar amounts.
     '''
    )
car = input('Lamborghini Tune-Ups:')
cat = int(car)
rent = int(input('Minhattan Apartment:'))
jet = int(input('Private Jet Rental:'))
gifts = int(input('Gifts:'))
food = int(input('Dining Out:'))
staff = int(input('staff (butlers, chef, driver, assistant):'))
guru = int(input('Personal Guru and Coach:'))
games = int(input('computer games:'))
total = car + rent + jet + gifts + food + staff + guru + games
print('\nGrand total:', total)
input('\n\nPress the enter key to exit.')

