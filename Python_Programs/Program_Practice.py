# # Write a Python function to check if a number is even or odd.
# num= int(input("Enter the number here: "))
# if num%2 == 0:
#     print(f"The number {num} is even number")
# else:
#     print(f"The number {num} is odd number")
#


# #Write a program to reverse a string.
# word = input("Enter the word here: ")
# word1=""
# for i in range(len(word)-1,-1,-1):
#     word1+=word[i]
# print(word1)
#and
# word = input("Enter the number here: ").split()
# list1=[]
# word1=""
# for i in word:
#     list1.append(i)
# for j in range(len(list1)-1,-1,-1):
#     word1+=list1[j] + " "
# print(word1)


#Implement a function to count the frequency of each word in a sentence.
# word= input("Enter the word here: ")
# dict={}
# for i in word:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
## and
# word= input("Enter the word here: ")
# dict={}
# for i in word:
#     if i == " ":
#         continue
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

#[2,1,5,4,6]
# #Write a program to find the second largest number in a list.
# list1= list(map(int,input("Enter the value here: ").split()))
# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if list1[i] > list1[j]:
#             list1[i],list1[j] = list1[j],list1[i]
# print(list1[-2])

# # Write a function that returns the Fibonacci sequence up to n terms.
#
# num = int(input("Enter the number here: "))
# a=0
# b=1
# print(f"{a}\n{b}")
# for i in range(num):
#     c = a + b
#     a = b
#     b = c
#     print(c)


# #Write a function that returns the factorial of a number using recursion.
# def fact(num):
#     if num<0:
#         print("Please enter a valid number! ")
#     elif num==1:
#         return 1
#     else:
#         return num * fact(num-1)
#
# num= int(input("Enter the fact number here: "))
# a=fact(num)
# print(a)

# # Write a Python program to find the second largest number in a list.
# list1 = list(map(int,input("Enter the number here: ").split()))
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] > list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
# print(list1[-2])

# #Given a string, write a function to check if it's a palindrome.
# word = input("Enter the string here: ")
# org = word
# rev = ""
# for i in range(len(word)-1,-1,-1):
#     rev+= word[i]
# if rev == org:
#     print(f"The given string {word} is a palindrome!")
# else:
#     print(f"The given string {word} is not a palindrome!")

# #Implement a function that removes duplicates from a list without using set().
# list1 = list(map(int,input("Enter the list value here: ").split()))
# list2 = []
# for i in list1:
#     if i not in list2:
#       list2.append(i)
# print(list2)

# # Write a function to count vowels in a string.
# word = input("Enter the word here: ").lower()
# vowels = "aeiou"
# count = 0
# for i in word:
#     if i in vowels:
#         count += 1
# print(count)

# # Given a list of integers, write a function to return the most frequent element.[1 2 1 3 4 1]
# list1 = list(map(int,input("Enter the value here: ").split()))
# maxcount = 0
# for i in range(len(list1)):
#     counts = 0
#     for j in range(len(list1)):
#         if list1[i] == list1[j]:
#             counts += 1
#     if counts > maxcount:
#         maxcount = counts
#         most_frequent = list1[i]
# print(most_frequent)
# or
# list1 = list(map(int,input("Enter the value here: ").split()))
# counts=0
# maxcount=0
# for i in list1:
#     counts = list1.count(i)
#     if counts > maxcount:
#         maxcount = counts
#         most_frequent = i
# print(most_frequent)

# # Write a function to check if a string is a pangram.
# word = input("Enter the sentence here: ").lower()
# value = 'abcdefghijklmanopqrstuvwxyz'
# word1=""
# for i in word:
#     if i in value and i not in word1:
#         word1+=i
#
# if len(word1) ==26:
#     print("A string is a pangram.")
# else:
#     print("A string is not a pangram.")
#

# # Write a Python function to compute the sum of digits in a number.
# num = input("Enter the number here: ")
# sum=0
# for i in num:
#     sum+=int(i)
# print(sum)
# or
# num = int(input("Enter the number here: "))
# sum= 0
# while num != 0:
#     dig = num % 10
#     sum += dig
#     num//=10
# print(sum)

#=======================
# num = int(input("Enter the number here: "))
# preVal= 0
# #sum1=0
# for i in range(1, num):
#     print(f"{preVal} + {i} = {preVal+i}")
#     preVal+=1

# list1 = list(map(int,input("Enter the number here: ").split()))
# list2=[]
# for i in list1:
#     if i % 5 ==0:
#         list2.append(i)
# print(list2)
#
# sentence = input("Enter the sentence here: ").split()
# count=0
# sentence1 = sentence[0]
# for i in sentence:
#     if sentence1 in i:
#             count+=1
# print(count)
# #
# #
#
# list1 = list(map(int,input("Enter the value: ").split()))
# list2 = list(map(int,input("Enter the value: ").split()))
# list3=[]
# for i in list1:
#     if i % 2 != 0:
#         list3.append(i)
# for j in list2:
#     if j % 2 == 0:
#         list3.append(j)
# print(list3)

#
    # num = int(input("Enter the number here: "))
    # for i in range(1,num+1):
    #     for j in range(1,num+1):
    #          print(i*j, end=" ")
    #     print("")
#
# salary = int(input("Enter the salary here: "))
# amount1 = salary - 10000
# sum1= (salary - amount1)*5/100
# print(sum1)
# amount2 = amount1-10000
# sum2 = (amount1 - amount2)*15/100
# print(sum2)
# amount3 = amount2 - 10000
# sum3 = (amount2 - amount3)*20/100
# print(sum3)
# total_sum = sum1 + sum2 + sum3
# print(f"Total tax deductions are: {total_sum}")
#
# word = input("Enter the word here: ")
# if word[0] == word[-1]:
#     print(True)
# else:
#     print(False)

# #Write a function to find all pairs in a list that sum to a given target.
# list1 = list(map(int,input("Enter the list value here : ").split()))
# target = int(input("Enter the target value: "))
# list2=[]
# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] + list1[j] == target:
#             list2.append((list1[i], list1[j]))
# print(list2)

#
# word = input("Enter the word here: ")
# word1=""
# for char in word:
#     if char == word[0]:
#         word1+=char.upper()
#     else:
#         word1+=char
# print(word1)

# celsius = float(input("Enter the value here: "))
# forhenhights = (celsius * 9/5) + 32
# print(forhenhights)

#========================================================
# list1 = list(map(int,input("Enter the value: ").split()))
# target = int(input("Enter the value: "))
#
# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[i] + list1[j] == target:
#             print(True)
#             exit()

#==========Pattern=====================
#Left-Aligned Right-Angled Triangle
# row = int(input("Enter the number of rows: "))
# for i in range(1,row+1):
#     print("*" * i)

# #Right-Aligned Right-Angled Triangle
# row = int(input("Enter the number of rows: "))
# for i in range(1,row+1):
#     print(" "*(row - i) +"*" * i)

# Inverted Left-Aligned Triangle
# row = int(input("Enter the number of rows: "))
# for i in range(row,0,-1):
#     print("*" * i)

# # Inverted Right-Aligned Triangle
# row = int(input("Enter the number of rows: "))
# for i in range(row,0,-1):
#     print(""*(row-1) + "*" * i)

# # Pyramid Pattern
# row = int(input("Enter the number of rows: "))
# for i in range(1,row+1):
#     print(" " * (row - i -1) + "* " * (2 * i + 1))

# # Inverted Pyramid
# row = int(input("Enter the number of rows: "))
# for i in range(row-1,-1,-1):
#     print(" " * (row - i - 1) + "* " * (2 * i +1))

# # Diamond Pattern
# row = int(input("Enter the number of rows: "))
# for i in range(1,row+1):
#     print(" " * (row - i - 1) + "* " * (2 * i + 1))
# for i in range(row-2,-1,-1):
#     print(" " * (row - i - 1) + "* " * (2 * i + 1))

# # Square Pattern
# row = int(input("Enter the number of rows: "))
# for i in range(row):
#     print("*" * row)
#
# n=16
# for i in range(n):
#         for j in range(n):
#            if i == 0 or i ==n-1 or j == 0 or j == n-1 or i==j or j==n-i-1 or i==round(n/2):
#                print("*",end=" ")
#            else:
#                print(" ",end=" ")
#         print()

#=====================================[3,4,6,7]

# list1 = list(map(int,input("Enter the number here: ").split()))
# list2= []
# counts=0
# for i in list1:
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         list2.append(i)
# print(list2)

# # nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nested_list = [1, [2, 3], [4, 5,[11, 22], 6], 7, [8, 9]]
# new_list = []
#
# for i in nested_list:
#     if type(i) == list:
#         for j in i:
#             if type(j) == list:
#                 for k in j:
#                     new_list.append(k)
#             else:
#                 new_list.append(j)
#     else:
#         new_list.append(i)
# print(new_list)
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
#
# # Add dict2 into dict1
# for key in dict2:
#     dict1[key] = dict2[key]
#
# print("Updated dict1:", dict1)

# Write a Python function to calculate the square of each number in a list.[3,4,5,6]
# list1 = list(map(int,input("Enter the value here: ").split()))
# disc={}
# for i in list1:
#     squa = i*i
#     disc[i] = squa
# print(disc)

# Write a Python program to count the number of words in a sentence.

# word = input("Enter the sentence: ").split()
# counts=0
# for i in word:
#     counts+=1
# print(counts)

# #  Implement a simple calculator that performs addition, subtraction, multiplication, and division.
# value1 = int(input("Enter the value here: "))
# value2 = int(input("Enter the value here: "))
# operators = input("Select the operators(+,-,*,/): ")
# if operators == "+":
#     sum1 = value1 + value2
#     print(f"The sum of value is: {sum1}")
# elif operators == "-":
#     sub1 = value1 - value2
#     print(f"The subtraction of value is: {sub1}")
# elif operators == "*":
#     mul1 = value1 * value2
#     print(f"The multiplication of value is: {mul1}")
# elif operators == "/":
#     div1 = value1 / value2
#     print(f"The division of value is: {div1}")
# else:
#     print("Please select the valid operator! ")
#
# # Write a Python function to generate all prime numbers up to n.
# num = int(input("Enter the number: "))
# if num <= 1:
#     print("Please! enter the correct input!")
# else:
#     for i in range(2,num):
#         if num%i != 0:
#             print("The number is prime number!")
#             break
#         else:
#             print("The number is not a prime number!")
#             break

# Given a list of n-1 integers in range 1 to n, find the missing number.
# 🧠 Input: [1, 2, 4, 6, 3, 7, 8]

# list1 = list(map(int,input("Enter the number here: ").split()))
# list2=[]
# minVal = min(list1)
# maxVal = max(list1)
#
# for i in range(minVal, maxVal+1):
#     if i not in list1:
#         list2.append(i)
# print(list2)

# 1. Find the Longest Substring Without Repeating Characters
#
# Input: "abcabcbb"
# Output: abc

# word = input("Enter the word here: ")
# word1=""
# for i in word:
#     if i not in word1:
#         word1+=i
# print(word1)

# # Write a program to find the sum of elements in a list.
# list1 = list(map(int,input("Enter the value here: ").split()))
# sumVal=0
# for i in list1:
#     sumVal+=i
# print(f"The sum of values are: {sumVal}")
#

# #Write a Python function to check whether a character is a vowel or a consonant.
# word = input("Enter the word here: ").lower()
# vowel = "aeiou"
# for i in word:
#     if i in vowel:
#         print(f"The vowel words are: {i}")
#     else:
#         print(f"The consonant words are: {i}")

# # Find the First Non-Repeating Character in a String swiss
# word = input("Enter the word here: ")
#
# for i in word:
#     counts = 0
#     for j in word:
#         if i == j:
#             counts += 1
#     if counts == 1:
#         print(i)
#         break
#Find All Pairs With a Given Difference
#🔹 Input: list = [1, 5, 3, 4, 2], difference = 2
# #
# list1 = list(map(int,input("Enter the nuber here: ").split()))
# list2=[]
# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[i] - list1[j] == 2:
#             list2.append((list1[i],list1[j]))
# print(list2)

# intersection
#
# list1 = list(map(int,input("Enter the value here: ").split()))
# list2 = list(map(int,input("Enter the value here: ").split()))
# intersecti = []
# for i in list1:
#     if i in list2 and i not in intersecti:
#         intersecti.append(i)
# print(intersecti)

# # Write a Python program to find the longest word in a given sentence.
# sentence = input("Enter the sentence here: ").split()
# word = ""
# maxcount = 0
# for i in sentence:
#     counts = 0
#     for j in i:
#         counts += 1
#     if counts > maxcount:
#         maxcount = counts
#         maxWord = i
# print(maxWord)


# #Write a program to print the multiplication table of a number.
# num = int(input("Enter the number here: "))
#
# for i in range(1, 11):
#     print(f"The multiplication would be:- {num} * {i} = {num*i} ")

# #Write a Python program to find the average of numbers in a list.
# list1 = list(map(int,input("Enter the number: ").split()))
# counts = len(list1)
# sum1 = 0
# for i in list1:
#     sum1 += i
# avg = sum1/counts
# print(avg)

# Write a function to calculate the running sum of a list.
# num = list(map(int,input("enter the number here: ").split()))
# total = 0
# list1 = []
# for i in num:
#     total += i
#     list1.append(total)
# print(list1)

# Given a string, return the first non-repeating character.
# word = input("Enter the word here: ")
#
# for i in word:
#     counts = 0
#     for j in word:
#         if i == j:
#             counts += 1
#     if counts == 1:
#         print(i)
#         break

# Write a Python function to check whether a given year is a leap year.
#
# year = int(input("Enter the year here: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year!")
# else:
#     print("not a Leap Year!")

# Write a Python program to convert a number to binary.
# num = int(input("Enter the number here: "))
# binary = ""
# while num > 0:
#     dig = num % 2
#     binary += str(dig)
#     num //= 2
# print(binary)

# Write a function to check if a list is sorted.
# list1 = list(map(int,input("Enter the number here: ").split()))
#
# for i in range(len(list1)-1):
#     if list1[i] > list1[i+1]:
#         print(False)
#         break
# else:
#     print(True)

#  Write a function to find the common elements in three sorted arrays.
# list1 = list(map(int,input("Enter the elements: ").split()))
# list2 = list(map(int,input("Enter the elements: ").split()))
# list3 = list(map(int,input("Enter the elements: ").split()))
# list4 = []
#
# for i in list1:
#     if i in list2 and i in list3 and i not in list4:
#         list4.append(i)
# print(list4)

# num = int(input("Enter the number: "))
# d = {}
# for i in range(1, num+1):
#     d[i] = i**2
# print(d)

##############
# Build a dictionary that counts character frequencies without using collections.

# word = input("Enter the word: ").split()
# d = {}
# for i in word:
#     counts = 0
#     for j in word:
#         if i == j:
#             counts += 1
#         d[i] = counts
# print(d)

#Replace digits with their word equivalents
#Input: "Surlav123" → Output: "SurlavOneTwoThree"
# word = input("Enter the word: ")
# inword = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
# word1 = ""
# for i in word:
#     if i.isdigit():
#         word1+= inword[int(i)]
#     else:
#         word1 += i
# print(word1)

# Return the first repeated word in a sentence.
# word = input("Enter the sentence here :").split()
# for i in range(len(word)):
#     for j in range(i + 1, len(word)):
#         if word[j] == word[i]:
#             print(word[i])
#             break
#     else:
#         continue
#     break

# Snake-like pattern print in list
# Input: [[1,2,3],[4,5,6],[7,8,9]] → Output: 1 2 3 6 5 4 7 8 9
# intp = [[1,2,3],[4,5,6],[7,8,9]]
# list1 = []
# word =""
#
# for i in intp:
#     if type(i) == list:
#         for j in i:
#             list1.append(j)
#     else:
#         list1.append(i)
# for k in list1:
#     word += str(k) + " "
# print(word)

#Flatten Deeply Nested List (Recursive or Stack)
#Input: [1, [2, [3, [4]], 5]] → Output: [1, 2, 3, 4, 5]

# list1 = [1, [2, [3, [4]], 5]]
# list2 = []
#
# for i in list1:
#     if type(i) == list:
#         for j in i:
#             if type(j) == list:
#                 for k in j:
#                     if type(k) == list:
#                         for l in k:
#                             list2.append(l)
#                     else:
#                         list2.append(k)
#             else:
#                 list2.append(j)
#     else:
#         list2.append(i)
# print(list2)

#Find smallest missing positive integer in unsorted list
#Input: [3, 4, -1, 1] → Output: 2

# list1 = [3, 4, -1, 1]
# list2 = []
# word = 0
# minL = min(list1)
# maxL = max(list1)
#
# for i in range(minL, maxL+1):
#     if i not in list1:
#         list2.append(i)
# for j in list2:
#     if j > 0:
#         word += j
# print(word)

#Zig-Zag List Merge
#Merge two lists such that one goes in forward order, the second in reverse:
#Input: [1,2,3] & [4,5,6] → Output: [1,6,2,5,3,4]

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = []
#
# for i in range(len(list1)):
#     list3.append(list1[i])
#     list3.append(list2[-(i + 1)])
# print(list3)

#Find all triplets with sum = 0 (no duplicate triplets)
#Input: [-1, 0, 1, 2, -1, -4] → Output: [[-1, -1, 2], [-1, 0, 1]]

# list1 = [-1, 0, 1, 2, -1, -4]
# target = 0
# list2 = []
#
# for i in list1:
#     for j in list1:
#         for k in list1:
#             if i != j and j != k and i != k:
#                 if i - j - k == target:
#                     if (i,j,k) not in list2:
#                         list2.append((i,j,k))
# print(list2)

#Print all unique combinations of 1,2,3 using all digits once
#Output: 123, 132, 213, 231, 312, 321

# list1 = list(map(int,input("Enter the value here: ").split()))
#
# for i in list1:
#     for j in list1:
#         if i != j:
#             for k in list1:
#                 if i != k and j != k:
#                     print(f"{i}{j}{k}")

# # every first character of a word should be capital letter
#
# word = input("Enter the words: ").split()
# word1 = ""
#
# for i in word:
#     for j in range(len(i)):
#         if j == 0:
#             word1 += i[j].upper()
#         else:
#             word1 += i[j].lower()
#     word1 += " "
# print(word1)
#
#
#word = input("Enter the word here: ")
#
# for i in range(len(word)):
#     for j in range(len(word)):
#         if i != j:
#             for k in range(len(word)):
#                 if i != k and j != k:
#                     for l in range(len(word)):
#                         if i != l and j != l and k != l:
#                             for m in range(len(word)):
#                                 if i != m and j != m and k != m and l != m:
#                                     for n in range(len(word)):
#                                         if i != n and j != n and k != n and l != n and m != n:
#                                             print(f"{word[i]}{word[j]}{word[k]}{word[l]}{word[m]}{word[n]}")


# word = input("Enter the word here: ")
# if len(word) == 8:
#     for ch in range(100):
#         for i in range(len(word)):
#             for j in range(len(word)):
#                 if i != j:
#                     for k in range(len(word)):
#                         if i != k and j != k:
#                             for l in range(len(word)):
#                                 if i != l and j != l and k != l:
#                                     for m in range(len(word)):
#                                         if i != m and j != m and k != m and l != m:
#                                             for n in range(len(word)):
#                                                 if i != n and j != n and k != n and l != n and m != n:
#                                                     for o in range(len(word)):
#                                                         if i != o and j != o and k != o and l != o and m != o and n != o:
#                                                             for p in range(len(word)):
#                                                                 if i != p and j != p and k != p and l != p and m != p and n != p and o != p:
#                                                                     print(word[i],word[j],word[k],word[l],word[m],word[n],word[o],word[p])
# else:
#     print("Please enter 8 character")


# list1 = list(map(int, input("Enter the value here: ").split()))
# for i in range(len(list1)):
#     for j in range(i+1, len(list1)):
#         if list1[i] > list1[j]:
#             list1[i],list1[j] = list1[j], list1[i]
# print(list1)


# word = input("Ente the word : ")
# d ={}
# for i in word:
#     counts=0
#     for j in word:
#         if i == j:
#             counts += 1
#         d[i] = counts
# print(d)

# word1 = input("Enter the word: ")
# word2 = input("Enter the second word: ")
# is_anagram = True
#
# if len(word1) != len(word2):
#     is_anagram = False
# else:
#     for i in word1:
#         if i not in word2:
#             is_anagram = False
#             break
#
# if is_anagram:
#     print("The word is an anagram !")
# else:
#     print("The word is not an anagram!")

word = input("Ente the word : ")
d ={}
for i in word:
    counts=0
    for j in word:
        if i == j:
            counts += 1

        d[i] = counts
print(d)