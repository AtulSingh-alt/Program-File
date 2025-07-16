# Count the number of digits using function
def count_digit(num):
    count=0
    while num!=0:
        num= num//10
        count= count+1
    return (f"The number of digits are: {count}")

num= int(input("Enter the number here: "))
print(count_digit(num))
