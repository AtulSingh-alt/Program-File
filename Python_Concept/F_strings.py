'''name="Atul"
age=30
height=2.4

print(f"My name is {name}, I am {age} years old and my height is {height} meters")
print(f"His father is {age*2} years old")
'''

age = int(input("Enter your current age: "))

years_left = 90- age
days_left = years_left * 365
months_left = years_left * 12
week_left = years_left * 52

print(f"You have {days_left} days, {week_left} weeks and {months_left} months left.")