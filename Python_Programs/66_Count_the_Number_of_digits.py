# Count the Number of Digits in a Number
num = int(input("Enter the number here: "))
count = 0
while num>0:
    count+=1
    num= num//10
print(f"The number of digits are: {count}")