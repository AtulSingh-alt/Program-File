# 32) Sum of natural number using Recursion

def NNS(n):
    if n <=1:
        return n
    else:
        return (n)+NNS(n-1)
n = int(input("Enter the number here :"))
if n <= 0:
    print("Enter the positive number!")
else:
    print(f"the sum of natural number upto given number is : {NNS(n)}")
