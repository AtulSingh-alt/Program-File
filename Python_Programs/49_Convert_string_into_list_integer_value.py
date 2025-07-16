# 48) Convert string to list in integer value
a = input("Enter the number: ")
b = []
for i in range(len(a)):
    b.append(int(a[i]))
print(b)
