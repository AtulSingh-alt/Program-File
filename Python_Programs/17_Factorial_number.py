#  Factorial number
numbers = int(input("Enter the number for factorial :"))
fact = 1
if numbers >0:
    for i in range(1, numbers+1):
        fact = fact * i
print(f"Your number {numbers} of factorial is : {fact}")