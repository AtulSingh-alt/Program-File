# user_pin = input("Please enter your pin code : ")
# if user_pin == 3344:
#     user_pin1 = int(user_pin)
#     withdraw_amt = int(input("Please enter the amount : "))
#     if withdraw_amt <= 10000:
#         amount = 10000 - withdraw_amt
#         print(f"Withdraw Success and your balance amount is : {amount}")
#     else:
#         print("You have an insufficient Balance!")
# else:
#     print(f"Please enter the correct Pin!")

row1 = [23,42,43] #input("Enter the value in list format : ")
row2 = [34,56,21] #input("Enter the value in list format : ")
row3 = [32,56,67] #input("Enter the value in list format : ")
matrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position= input("Enter the position where you want to hide : ")
row_number = int (position[0])
column_number = int(position[1])
row_selected = matrix[row_number-1]
row_selected[column_number-1] = 'x'
print(f"{row1}\n{row2}\n{row3}")