# Print all the prime numbers

lower = int(input("Enter the lower number to find it is prime number or not : "))
upper = int(input("Enter the upper number to find it is prime number or not : "))
for number in range(lower,upper+1):
    if number <= 1:
        print(f"You entered year is {number} and it is not a prime number !")
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(f"You entered year is {number} and it is a prime number !")