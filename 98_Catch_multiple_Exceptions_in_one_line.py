# Catch multiple Exceptions in one line
string = input("Enter something here :")

try:
    num= int(input("Enter a number here: "))
    print(string + num)
except(ValueError,TypeError) as a:
    print(a)
