# 28) Factor of a number

num = int(input("Enter the number here : "))
for i in range(1,num+1):
    if num%i == 0:
        print(f"The factor number of {num} is: {i}")
