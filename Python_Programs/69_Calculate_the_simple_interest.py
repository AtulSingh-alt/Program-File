# Program to Find Simple Interest
principle=float(input("Enter the principle amount: "))
time=float(input("Enter the time(years): "))
rate=float(input("Enter the rate: "))
simple_interest=(principle*time*rate)/100
print("The simple interest is:",simple_interest)