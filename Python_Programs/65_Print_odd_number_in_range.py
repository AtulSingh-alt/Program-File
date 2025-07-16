# Print All Odd Numbers in a Range
lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))
for i in range(lower,upper+1):
    if(i%2 != 0):
        print(i)