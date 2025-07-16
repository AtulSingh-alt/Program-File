# 22) Display powers of 2

num = int(input("Enter the number of terms here : "))
list1 = []
for num in range(num+1):
    result = 2 ** num
    list1.append(result)
    print(f"The value of 2 raised to power {num} is {result}")
print(list1)
