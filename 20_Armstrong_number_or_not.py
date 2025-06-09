# 19) Armstrong number or not
numbers = int(input("Enter the value : "))
sum = 0
temp = numbers

while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum = sum + cube
    temp = temp // 10

if sum == numbers:
    print("It is an armstong number!")
else:
    print("It is not an armstong number!")
