sam_details = {
    "Name" : 'sam',
    'Adr' : '123456',
    'pan': 'RJRPS2275G',
    'ATMPIN' : '2705',
    'Balance' : 10000
}
All_attempts = 3
while All_attempts > 0:
    user_pin = input('Enter your atm pin:')
    if user_pin in sam_details['ATMPIN']:
        print('welcome canara atm')
        choice_ = int(input('Enter \n1.Withdraw \n2.Deposit \n3.Balance Enquiry:'))
        if choice_ == 1:
            withdraw_amount = int(input('Enter the amount to withdraw:'))
            if withdraw_amount <= sam_details['Balance'] and withdraw_amount % 100 ==0:
                sam_details['Balance'] -= withdraw_amount
                print(f'please collect your cash and your remaining balance is {sam_details["Balance"]}')
            else:
                print('Insufficient balance or enter the amount in multiples of 100')
        elif choice_ == 2:
            deposit_amount = int(input('Enter the amount to deposit:'))
            if deposit_amount % 100 == 0:
                sam_details['Balance'] += deposit_amount
                print(f'Your amount is deposited and your new balance is {sam_details["Balance"]}')
            else:
                print('Please enter a valid amount to deposit')
        elif choice_ == 3:
            print(f'Your current balance is {sam_details["Balance"]}')
        break
    else:
        All_attempts -= 1
        if All_attempts > 0:
            print(f'Incorrect pin entered and you have {All_attempts} attempts' )
        else:
            print('your card is blocked...')