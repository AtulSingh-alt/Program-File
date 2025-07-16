# find the number is Prime number or not

number = int(input("Enter the number to find it is prime number or not : "))
if number <= 1:
    print(f"You entered year is {number} and it is not a prime number !")
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f"You entered year is {number} and it is not a prime number !")
            break
    else:
            print(f"You entered year is {number} and it is a prime number !")