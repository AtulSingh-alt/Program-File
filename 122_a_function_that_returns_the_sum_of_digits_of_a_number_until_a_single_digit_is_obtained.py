# a function that returns the sum of digits of a number until a single digit is obtained
number = int(input("Enter the number here :"))
sum = 0

for dig in str(number):
   sum += int(dig)

while(len(str(sum))>1):
   temp = 0
   for dig in str(sum):
       temp += int(dig)
   sum = temp

print(sum)