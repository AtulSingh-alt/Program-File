# 33) Find the factrorial of number using recursion

def FON(n):
    if n <=1:
        return n
    else:
        return (n)*FON(n-1)
n = int(input("Enter the number here :"))
if n<=0:
    print("Enter the positive number!")
else:
    print(f"The factorial number upto given number is : {FON(n)}")