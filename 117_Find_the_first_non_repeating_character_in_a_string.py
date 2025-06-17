# Find the first non-repeating character in a string
string = input("Enter the word here: ")
dict = {}
result = -1
for char in string:
   if char in dict.keys():
      dict[char] += 1
   else :
      dict[char] = 1

for key in dict:
  if dict[key] == 1:
       result = key
       break

print(result)