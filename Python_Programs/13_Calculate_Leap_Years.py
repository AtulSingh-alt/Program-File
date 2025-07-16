# calculate the Leap year

year = int(input("Enter the year : "))
if year%4 == 0 and year%100 != 0:
    print(f"You entered year is {year} and it is leap year !")
elif year%400 == 0:
    print(f"You entered year is {year} and it is leap year !")
else:
    print(f"You entered year is {year} and it is not a leap year !")