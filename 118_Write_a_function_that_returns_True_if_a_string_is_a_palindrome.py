# Write a function that returns True if a string is a palindrome
string = input("Enter the word here :")
newS1 = ""
newS2 = ""

for char in string:
   if char == " ":
        continue
        newS1 += char.lower()

for i in range(len(newS1)-1, -1, -1):
    newS2 += newS1[i]

print(newS1 == newS2)