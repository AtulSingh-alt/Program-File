# 21) Sum of natural numbers
num = int(input("Enter the value for sum here :"))

if num<0:
    print("Please enter the positive value!")
else:
    sum =0
    while num>0:
        sum += num
        num-=1
    print(sum)
