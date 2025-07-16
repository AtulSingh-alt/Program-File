# Program for find the number of the days in a month
# def leap_year(year):
#     if year % 4 ==0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# def days_in_month(year,month):
    #     days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
#     if leap_year(year) and month==2:
#         return 29
#     else:
#         return days_list[month-1]
#
# year=int(input("Enter a year: "))
# month=int(input("Enter a month: "))
# print(days_in_month(year,month))


# # Calculator with the use of dictionary
# import os
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
# operations_dict={
#     "+":add,
#     "-":subtract,
#     "*":multiply,
#     "/":divide
# }
# def calculator():
#     number1=int(input("Enter the first number: "))
#     for symbol in operations_dict:
#         print(symbol)
#
#     continue_flag=True
#     while continue_flag:
#         op_symbol = input("Pick an operation: ")
#         number2 = int(input("Enter the second number: "))
#         calculator_fun = operations_dict[op_symbol]
#         output = calculator_fun(number1, number2)
#         print(f"{number1} {op_symbol} {number2}={output}")
#
#         should_continue = input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit: ").lower()
#         if should_continue == 'y' or should_continue == 'Y':
#             number1 = output
#         elif should_continue=='n':
#             continue_flag=False
#             os.system('cls')
#             calculator()
#         else:
#                 continue_flag=False
#                 print("Bye")
# calculator()
#

# # Program-Guess the number
# import random
#
# EASY_LEVEL_ATTEMPTS=10
# HARD_LEVEL_ATTEMPTS=5
# def set_difficulty(level_chosen):
#     if level_chosen=='easy':
#         return EASY_LEVEL_ATTEMPTS
#     elif level_chosen=='hard':
#         return HARD_LEVEL_ATTEMPTS
#     else:
#         return
#
# def check_answer(guessed_number,answer,attempts):
#     if guessed_number<answer:
#         print("Your guess is too low")
#         return attempts-1
#     elif guessed_number>answer:
#         print("Your guess is too high")
#         return attempts-1
#     else:
#         print(f"Your guess is right... The answer was {answer}")
#
# def game():
#     print("Let me think of a number between 1 to 50.")
#     answer=random.randint(1,50)
#     print(answer)
#     level=input("Choose level of difficulty...type 'easy' or 'hard': ")
#     attempts=set_difficulty(level)
#     if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
#         print("You have entered wrong difficulty level.. Play again!!")
#         return
#     guessed_number=0
#     while guessed_number != answer:
#         print(f"You have {attempts} remaining to guess the number.")
#         guessed_number = int(input("Guess a number: "))
#         attempts = check_answer(guessed_number, answer, attempts)
#         if attempts==0:
#             print("You are out of guesses...you lose!")
#             return
#         elif guessed_number != answer:
#             print("Guess again")
#
# game()

# Program for coffee machine
menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":150
    },
    "espresso":{
            "ingredients":{
                "water":50,
                "coffee":18
            },
            "cost":100
        },
    "cappuccino":{
            "ingredients":{
                "water":250,
                "milk":100,
                "coffee":24
            },
            "cost":200
        },
}
profit=0
resources={
    "water":500,
    "milk":200,
    "coffee":100
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert coins.")
    total=0
    coins_five=int(input("How many 5rs coin?: "))
    coins_ten = int(input("How many 10rs coin?: "))
    coins_twenty = int(input("How many 20rs coin?: "))
    total=coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successful(money_received, coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit+=coffee_cost


is_on=True
while is_on:
    choice=input("What would you like to have? (latte/espresso/cappuccino): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money=Rs {profit}")
    else:
        coffee_type=menu[choice]
        print(coffee_type)
    if check_resources(coffee_type['ingredients']):
        payment=process_coins()
        is_payment_successful(payment,coffee_type['cost'])

