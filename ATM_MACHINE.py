#accouunt balance
balance = 100

# Welcome message
# def incorrect_pin():
#     print('Incorrect pin entered 3 times. \n'
#           ' Card has been blocked.\n'
#           'Please contact CFG ')
def welcome():
    print('\033[1m' , '******Hello and Welcome to The CFG ATM***** \033[0m')

def pin():
    pin= {2903}
    count = 1 #sets the number for incorrect pin entered

    while True:
        try:
            entered_pin = int(input('Welcome ' + name  + ' Please enter your Four Digit Pin Code: \n'))
            if entered_pin not in pin:
                   raise ValueError('Incorrect pin entered  \n'
                                    'Please try again:  ')
            print('****************************************************************** \n'
                      '                 Correct Pin entered... \n'
                      '                 Your details are being processed \n'
                      '******************************************************************')
            break
        except ValueError:
            print('Incorrect pin entered')
            print()
            count += 1
            if count == 4:
                print('****************************************************************** \n'
                      '             Incorrect pin entered 3 times. \n'
                      '               Card has been blocked.\n'
                      '                 Please contact CFG \n'
                      '******************************************************************')
                quit()




def account_details():
    print('Account Name: ' '\033[1m', name ,'\033[0m')
    print()
    print('Account Balance:' '\033[1m', balance, '\033[0m')
    print()

def withdraw():
    withdraw = int(input('How much would you like to withdraw today: '))

    balance_remain = balance - withdraw
    if withdraw > 100:
                print('Insufficient funds available')
                again = input('Would you like to withdraw a different amount? (y/n): ')
                if again == 'y':
                        withdraw

                else:
                    again == 'n'
                    print('****************************************************************** \n'
                          'Thank you for using CFG Bank \n'
                          'Goodbye \n'
                          '******************************************************************')


    else:
        print('****************************************************************** \n'
            'Withdraw request accepted\n'
              '******************************************************************')
        print()
        print('Remaining balance: ', '\033[1m',  balance_remain, '\033[0m')
        print()
        print('Thank you for using our services. \n'
              'Please remove your card :)')
        quit()


welcome()
name = input('Please Enter Your Name: \n ')
pin()

while True:
        trans = input('Would you like to withdraw some money? (y/n): \n')
        if trans == 'y':

            account_details()
            withdraw()
        elif trans == 'n':
            print('****************************************************************** \n'
                  'Thank you for using CFG Bank \n'
                  'Goodbye \n'
                  '******************************************************************')
            quit()
        else:
            print('Wrong command!  Enter ' ,y,' for yes and ',n,' for NO.\n')

