# 34) Convert decimal to binary using recursion

def ConvertBinary(n):
    if n>1:
        ConvertBinary(n//2)
    print(n%2, end="")

n = int(input("Enter the number to convert in binary : "))
print("The binary number of given number is :")
ConvertBinary(n)
