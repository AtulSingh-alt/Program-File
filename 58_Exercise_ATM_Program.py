user_pin = input("Please enter your pin code : ")
if user_pin == 3344:
    user_pin1 = int(user_pin)
    withdraw_amt = int(input("Please enter the amount : "))
    if withdraw_amt <= 10000:
        amount = 10000 - withdraw_amt
        print(f"Withdraw Success and your balance amount is : {amount}")
    else:
        print("You have an insufficient Balance!")
else:
    print(f"Please enter the correct Pin!")