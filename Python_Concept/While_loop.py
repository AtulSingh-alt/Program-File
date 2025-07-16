# count = 1
# while count <5:
#     print(count)
#     count+=1
# else:
#     print("In else block")
# print("Out from loop")

# while loop termination for else statement
#
# count = 1
# while count <5:
#     print(count)
#     count+=1
#     if count == 3:
#         break
# else:
#     print("In else block")
# print("Out from loop")

# Take input from the user
number = int(input("Enter a number (-1 to quit) : "))
while number != -1:
    print(number)
    number = int(input("Enter a number (-1 to quit) : "))
else:
    print("In else Block")
print("out from the loop")