'''height = int(input("Enter the height :"))

if(height>3):
    print("Buy the token")
else:
    print("No Token Required")

#Even or ODD number

number = int(input("Enter the value :"))

if number % 2 == 0:
    print("The value is Even number")
else:
    print("The value is Odd number")

#Nested if else & elif

height = int(input("Enter your height in feet :"))

if height >= 3:
    print("You can ride")
    age = int(input("Enter your current age :"))
    if age <= 18:
        print("Pay 250 rupees")
    else:
        print("Pay 500 rupees")
else:
    print("You can't ride\nBye")

#elif condition
height = int(input("Enter your height in feet :"))

if height >= 3:
    print("You can ride")
    age = int(input("Enter your current age :"))
    if age <= 12:
        print("Pay 250 rupees")
    elif age <= 18:
        print("Pay 500 rupees")
    else:
        print("Pay 1000 rupees")
else:
    print("You can't ride\nBye")
print("Bye")

#BMI with elif

weight = float(input("Enter your weight in KG :"))
height = float(input("Enter your height in meter :"))

bmi = weight/height**2
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are Obese")
else:
    print(f"Your BMI is {bmi} and you are clinically Obese")

#Leap Year
year = int(input("Which year you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")

#Multiple If condition
height = float(input("What is your height? "))
bill = 0
if height >= 3:
    print("can ride")
    age= int(input("What is your age? "))
    if age < 12:
        bill = 150
        print("Ticket price is 150 Rs")
    elif age <= 18:
        bill = 250
        print("Ticket price is 250 Rs")
    else:
        bill = 500
        print("Ticket price is 500 Rs")

    want_photo = input("Do you want to take a photo (Y/N)? ")
    if want_photo == 'Y' or want_photo == 'y':
        bill = bill + 50

    print(f"Your total bill is {bill}")
else:
    print("can't ride")
print("Thank you.... Enjoy your ride")'''

# Love Calculator

name1 = input("What is your name? ")
name2 = input("What is his/her name? ")
combine_string = name1 + name2
lower_case_string = combine_string.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')
true = t + r + u + e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} and you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score} and you are alright together")
else:
    print(f"Your love score is {love_score}")