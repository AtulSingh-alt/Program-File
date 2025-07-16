import re
a= "charlie chchaplin coa and the chocolate factory"
b= "atul.singh@gmail.com"
c= "hello"
d= "xyz,yz,xyzz,xyyz,xxzzy,zyz,xxyyzz"

# match= re.search(r"\.",b)         #Use to drop the special character
# match= re.search(r"[l]",b)        # to match the character is present or not
# match= re.findall(r"[l]",c)
# match= re.search(r"^a",b)       # to match with start character
# match= re.search(r"com$",b)     # Matches with the end character
# match= re.findall(r"c.a",a)     #Match with any characters
# match= re.findall(r"cha|fac",a)     #match with any character along with OR
# match= re.search(r"cha|fac",a)
# match= re.findall(r"ch?a",a)        #Matches zero or one times occurrence
# match= re.findall(r"ch*a",a)    # Matches any number of occurrence
# match= re.findall(r"xy+z",d)    #One or more occurrence
# match= re.findall(r"x{2,4}",d)      #Indicate teh number of occurrences
# match= re.findall(r"(x|z)yz",d)    # Enclose the group of RegEx
#
# print(match)

import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"\bfox\b"  # Matches the word "fox"

match = re.search(pattern, text)
if match:
    print(f"Match found: {match.group()}")

matches = re.findall(r"\b\w{4}\b", text) # Matches words with exactly 4 characters
print(f"Matches found: {matches}")

new_text = re.sub(r"dog", "cat", text) # Replace "dog" with "cat"
print(f"New text: {new_text}")

split_text = re.split(r"\s", text) # Split by white space
print(f"Split text: {split_text}")