# Reverse a number
num = int(input("Enter the number here: "))
rev=0
while num != 0:
    dig = num%10
    rev = rev*10+dig
    num = num//10
print(f"Reverse number is: {rev}")