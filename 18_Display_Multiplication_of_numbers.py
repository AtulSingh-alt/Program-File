# Display multiplication number

numbers = int(input("Enter the number for factorial :"))
fact = 1
for i in range(1, numbers+1):
    print(f"{numbers} * {i} = {numbers * i}")
    fact = fact * i
print(f"Total is : {fact}")
