# Rain = input('Is it raining outside? y/n')
# if Rain == 'y':
#     print('Take an umbrella')
# elif Rain == 'n':
#     print('You do not need an umbrella')
#
# my_money =int(input('How much money do you have? '))
# boat_cost = 20+5
# if my_money >= boat_cost:
#     print('You can afford the boat hire')
# else:
#     print('You cannot afford the board hire')
#
#
# year_of_book = input('What Year was the book written')
# stringyear = str(year_of_book)
# century = stringyear[:2] + "00"
# century = int(century)
# if century == 18:
#     print ('Eigteenth Century')

year = int(input(' Please enter the year the book was written: '))
def find_century(year):
    # No negative value is allow for year
    if (year >= 1800 and year <= 1899):
        print('Nineteenth century')

    elif (year >= 1900 and year <= 1950 ):
        print('Twentieth century')
    else:
        print("We do not stock that book")
        return


def find_decade(year):
    cen = int(year / 100)
    decade = year - (cen * 100)

    if (year < 1800 and year > 1950):
        print('We do not stock that book')
    elif(decade <= 9 ):
        print('Noughties')
    elif (decade <= 19 and decade > 9):
        print('Tens')
    elif (decade <= 29 and decade > 19):
        print('Twenties')
    elif (decade <= 39 and decade > 29):
        print('Thirties')
    elif (decade <= 49 and decade > 39):
        print('Forties')
    elif (decade <= 59 and decade > 49):
        print('Fifties')
    elif (decade <= 69 and decade > 59):
        print('Sixties')
    elif (decade <= 79 and decade > 69):
        print('Seventies')
    elif (decade <= 89 and decade > 79):
        print('Eighties')
    else:
        print('Nineties')

if (year < 1800 and year > 1950):
    print('We do not stock that book')
else:
    find_century(year), find_decade(year)


