print(
    '''
                Trust Fund Buddy
     Totals your monthly spending so that your trust fund does not run out
     (and you are forced to get a real job).
     Please enter the requested, monthly costs. Since you are rich, ignore pennies and use only dollar amounts.
     '''
    )
car = input('Lamborghini Tune-Ups:')
rent = input('Minhattan Apartment:')
jet = input('Private Jet Rental:')
gifts = input('Gifts:')
food = input('Dining Out')
staff = input('staff (butlers, chef, driver, assistant):')
guru = input('Personal Guru and Coach:')
games = input('computer games:')
total = car + rent + jet + gifts + food + staff + guru + games

print('\nGrand total:', total)
input('\n\nPress the enter key to exit.')
