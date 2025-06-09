# 31) Display fibonacci sequence using Recursion

def fibo (n):
    if n <=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter the number here : "))
if n <=0:
    print("Enter the positive number!")
else:
    print("Fibonacci Sequence ")
    for i in range(n):
        print(fibo(i))
