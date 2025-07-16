# Set 1 = Basic Exercise for Beginners

# # Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# mul = num1 * num2
# if mul <= 1000:
#     print(f"The multiplication of two numbers are:{mul}")
# else:
#     sum = num1 + num2
#     print(f"The sum of two numbers are:{sum}")

# #Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
#
# num = int(input("Enter the number: "))
# preval = 0
# print(f"Printing current and previous number sum in a range({num}) ")
# for i in range(num):
#     print(f"Current Number {i} Previous Number {preval}   Sum: {preval+i}")
#     preval = i

# # Write a Python code to accept a string from the user and display characters present at an even index number.
#
# word = input("Enter the word here: ")
#
# for i in range(0,len(word)-1,2):
#     print(word[i])

# # Write a Python code to remove characters from a string from 0 to n and return a new string.
# word = input("Enter the word here: ")
# delchar = int(input("Enter the numer of char which you want to remove: "))
#
# if delchar < len(word):
#     print('Original string:', word)
#     x = word[delchar:]
#     print("Removing characters from a string")
#     print('New string:',x)
# else:
#     print("Delete char must be less than the length of the string.")

# # Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
#
# list1 = list(map(int,input("Enter the value here: ").split()))
# if list1[0] == list1[-1]:
#     print(True)
# else:
#     print(False)

# # Write a Python code to display numbers from a list divisible by 5
# list1 = list(map(int,input("Enter the value here: ").split()))
# for i in list1:
#     if i % 5 ==0:
#         print(i)

# # Write a Python code to find how often the substring “Emma” appears in the given string.
#
# sentence1 = input("Enter the sentence here: ").split()
# counts = 0
# for i in range(len(sentence1)):
#     if sentence1[i] == sentence1[0]:
#         counts += 1
# print(f"{sentence1[0]} appeared {counts} times")
#
# # or
#
# sentence1 = input("Enter the sentence here: ").split()
# counts = sentence1.count("Emma")
# print(counts)

# # Print the following pattern
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5
#
# num = int(input("Enter the row here: "))
#
# for i in range(1,num+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# # Write a Python code to check if the given number is a palindrome.
#
# num = input("Enter the number here: ")
# num1= ""
# for i in range(len(num)-1, -1, -1):
#     num1 += num[i]
# print(f"original number {num}")
# if num == num1:
#     print("Yes. given number is palindrome number")
# else:
#     print("No. given number is not palindrome number")

# # or
# num = int(input("Enter the number here: "))
# org = num
# sum = 0
#
# while num != 0:
#     dig = num % 10
#     sum = sum*10 + dig
#     num //= 10
# if sum == org:
#     print("Yes. given number is palindrome number")
# else:
#     print("No. given number is not palindrome number")

# # Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
#
# list1 = list(map(int,input("Enter the values here: ").split()))
# list2 = list(map(int,input("Enter the values here: ").split()))
# list3 = []
#
# for i in list1:
#     if i % 2 != 0:
#         list3.append(i)
# for j in list2:
#     if j % 2 == 0:
#         list3.append(j)
# print(list3)

# #  Get each digit from a number in the reverse order.
#
# num = input("Enter the number here: ")
# num2 = ""
#
# for i in range(len(num)-1,-1,-1):
#     num2 += num[i] + " "
# print(num2)

# # Calculate income tax
#
# salary = int(input("Enter the salary here: "))
# amount1 = salary - 10000
# sum1= (salary - amount1)
# # print(sum1)
# amount2 = amount1-10000
# sum2 = amount2 *10/100
# # print(sum2)
# amount3 = amount2 - 10000
# sum3 = amount2 *20/100
# # print(sum3)
# total_sum = sum1 + sum2 + sum3
# print(f"{sum1}*0% + {sum2}*10% + {amount2}*20% = ${total_sum}")

# # The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
#
# num = int(input("Enter the number here: "))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#          print(i*j, end=" ")
#     print("")
#

# # Print a downward half-pyramid pattern of stars
# # * * * * *
# # * * * *
# # * * *
# # * *
# # *
#
# row = int(input("enter the number of rows: "))
# for i in range(row):
#     for j in range(row-i):
#         print("*", end=" ")
#     print()

# # Get an int value of base raises to the power of exponent
# def power_of_exponent(base,expo):
#     num = expo
#     result = 1
#     while num > 0:
#         result *= base
#         num -= 1
#     print(base, "the raises to the power of", expo, "is:",result)
#
# power_of_exponent(2,5)

# #  Generate Fibonacci series up to 15 terms
# num = int(input("Enter the terms here: "))
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(num):
#     c = a + b
#     a = b
#     b = c
#     print(c)

# # Check if a given year is a leap year
# year = int(input("Enter the year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year!")
# else:
#     print("Not a leap year!")

# # Print Reverse Number Pattern
# # 1 1 1 1 1
# # 2 2 2 2
# # 3 3 3
# # 4 4
# # 5
#
# row = int(input("Enter the rows here: "))
# for i in range(1,row):
#     for j in range(row-i):
#         print(i, end=" ")
#     print()

# # Check if a user-entered string contains any digits using a for loop
#
# word = input("Enter the string here: ")
# for i in word:
#     if '0' <= i <= '9':
#         print("The string contains digits!")
#         break
# else:
#     print("The string doesn't contains digits!")

# # Capitalize the first letter of each word in a string
#
# sentence = input("Enter the sentence here: ").split()
# sentence1 = ""
# for i in sentence:
#     for j in range(len(i)):
#         if i[j] == i[0]:
#             sentence1 += i[j].upper()
#         else:
#             sentence1 += i[j]
#     sentence1 += " "
# print(sentence1)

# # Create a simple countdown timer using a while loop.
# import time
# seconds = int(input("Enter the seconds here: "))
# while seconds > 0:
#     print(f"Time remaining: {seconds} seconds")
#     time.sleep(1)
#     seconds -= 1
# print("Time's up!")


# Set 2 = Python Input and Output Exercise

# # Write a program to accept two integer numbers from the user and calculate their product.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the first number: "))
#
# mul = num1 * num2
# print(f"The multiplication of a number : {mul}")


# # Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.
# str1 = 'My'
# str2 = 'Name'
# str3 = 'Is'
# str4 = 'James'
# print(str1,str2,str3,str4,sep='**')

# # Display Decimal Number to Octal using print() function
# num = int(input("Enter the number: "))
# print('%o'% num)

# # Display Float Number with 2 Decimal Places
# num = float(input("Enter the number: "))
# print('%.2f'% num)

# # Accept a list of 5 float numbers as an input from the user
# # list1 = list(map(float,input("Enter the value here: ").split()))
# # print(list1)
# # or
# num = []
# for i in range(5):
#     print(f"Enter number at location {i} :")
#     value = float(input())
#     num.append(value)
# print(num)

# # Write a program to take three names as input from the user in a single call to the input() function.
# str1,str2,str3 = input("Enter the words here: ").split()
# print("Name1:", str1)
# print("Name2:", str2)
# print("Name3:", str3)

# # Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”. Based on the user’s input, perform the corresponding action
# user_inp = int(input("Select an option between 1 to 3: "))
#
# if user_inp == 1:
#     print("Hello User! ")
# elif user_inp == 2:
#     num = int(input("Enter the value here: "))
#     squ = num ** 2
#     print(f"The squar of number is : {squ}")
# elif user_inp == 3:
#     print("Ok, I am exiting the program!")
# else:
#     print("Please Enter the valid input!")

# # You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these lists as a simple table with columns “Name” and “Score”.
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]
#
# print(f"{'Name':<10} {'Score':<5}")
# print("-" * 15)
# for name, score in zip(names, scores):
#     print(f"{name:<10} {score:<5}")

# # Ask the user for a number. Print this number padded with leading zeros to a width of 5.
# number_str = input("Enter a number: ")
# padded_number = number_str.zfill(5)
# print(padded_number)

# Set 3 - Python Loop Exercise

# # Print first 10 natural numbers using while loop
# num = int(input("Enter the number here: "))
# for i in range(1,num+1):
#     print(i)

# # Write a Python code to print the following number pattern using a loop.
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5
#
# row = int(input("Enter the number fo rows here: "))
# for i in range(1,row+1):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()

# # Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# num = int(input("Enter the number here: "))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print("Sum is :",sum)

# # Print multiplication table of a given number
# num = int(input("Enter the number here: "))
# for i in range(1,11):
#     multi = num * i
#     print(multi)

# #Write a Python program to display only those numbers from a list that satisfy the following conditions
# #
# # The number must be divisible by five
# # If the number is greater than 150, then skip it and move to the following number
# # If the number is greater than 500, then stop the loop
#
# list1 = list(map(int, input("Enter the value here: ").split()))
# for i in list1:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)

# # Write a Python program to count the total number of digits in a number using a while loop.
# num = int(input("Enter the number here: "))
# counts = 0
# while num != 0:
#     num = num // 10
#     counts += 1
# print(counts)
# or
# num = input("Enter the number here: ")
# print(len(num))

# # Write a Python program to print the reverse number pattern using a for loop.
# # 5 4 3 2 1
# # 4 3 2 1
# # 3 2 1
# # 2 1
# # 1
#
# row = int(input("Enter the number here: "))
# for i in range(row,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=' ')
#     print()

# Print list in reverse order using a loop
list1 = list(map(int,input("Enter the values here: ").split()))
list2 = []
for i in range(len(list1)-1,-1,-1):
    print(list1[i])
