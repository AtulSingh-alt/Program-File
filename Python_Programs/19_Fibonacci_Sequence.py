# Fibonacci Sequence

numbers = int(input("Enter the value : "))
a = 0
b = 1
print(f"{a}\n{b}")
for i in range(2, numbers):
    c = a + b
    a = b
    b = c
    print(c)