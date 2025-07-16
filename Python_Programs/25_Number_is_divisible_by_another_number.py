# 24) Find the numbers is divisible by another number
numbers = int(input("Enter till the number : "))
div_num = int(input("Enter the divisible number : "))

for i in range(1,numbers+1):
    if i%div_num == 0:
        print(i)