import random
user_choice = int(input("Enter your choice : Type 0 for Rock, 1 for Paper, 2 for Sciossors: "))
if user_choice >= 3 or  user_choice < 0:
    print("You entered invalid number, You lose.")
else:
    computer_choice = random.randint(0, 2)
    print("Computer's choice :")
    print(computer_choice)
    if computer_choice == user_choice:
        print("It's a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice > user_choice:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You win")