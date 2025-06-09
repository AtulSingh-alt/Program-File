#6) Write the program for rock, Paper and Scissors
import random
from numbers import Number

user_Number = int(input("Enter the number which are 0 for Rock, 1 for Paper and 2 for Scissors : "))
if user_Number >=3 or user_Number <0:
    print("You have entered invalid number, Thank you")
else:
    computer_number = random.randint(0,2)
    print("Computer number is : ")
    print(computer_number)
    if computer_number == 0 and user_Number == 2:
        print("You lose")
    elif computer_number == 2 and user_Number == 0:
        print("You win")
    elif computer_number > user_Number:
        print("You lose")
    elif computer_number < user_Number:
        print("You win")
    elif computer_number == user_Number:
        print("it's draw")