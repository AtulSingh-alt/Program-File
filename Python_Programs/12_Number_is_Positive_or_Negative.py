# Number is positive or negative

number = int(input("Enter the number : "))
if number > 0:
    print(f"Your entered number is {number} and it is positive number!")
elif number == 0:
    print(f"Your entered number is {number} and it is zero number!")
else:
    print(f"Your entered number is {number} and it is negative number!")