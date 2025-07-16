#5) nested if-else program for booking pizza

order = input("Enter the size of Pizza which you want to order (Small Pizza/ Medium Pizza/ Large Pizza): ")
bill= 0

if order == "Small Pizza" or order == "small pizza":
    bill = 100
   # print("Your bill is 100 rupees")
elif order == "Medium Pizza" or order == "medium pizza":
    bill = 200
   # print("Your bill is 200 rupees")
elif order == "Large Pizza" or order == "large pizza":
    bill = 300
  #  print("Your bill is 300 rupees")
else:
    print("Please enter the valid pizza size... Thank you")
    exit()

want_extra = input("Do you want to take along with your select pizza? (Pepperoni / Extra Cheese): ")
if want_extra == 'Pepperoni' and order == 'Small Pizza':
    bill = bill + 30
    print(f"Your total bill is {bill}")
elif want_extra == 'Pepperoni' and order == 'Medium Pizza':
    bill = bill + 50
    print(f"Your total bill is {bill}")
elif want_extra == 'Pepperoni' and order == 'Large Pizza':
    bill = bill + 50
    print(f"Your total bill is {bill}")
elif want_extra == 'Extra Cheese' and order == 'Small Pizza':
    bill = bill + 20
    print(f"Your total bill is {bill}")
elif want_extra == 'Extra Cheese' and order == 'Medium Pizza':
    bill = bill + 20
    print(f"Your total bill is {bill}")
elif want_extra == 'Extra Cheese' and order == 'Large Pizza':
    bill = bill + 20
    print(f"Your total bill is {bill}")
else:
    print("Please enter the valid extra things... Thank you")
    exit()

print("Thank you for contacting us...")