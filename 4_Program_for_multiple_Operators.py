# 4) Program on Operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")