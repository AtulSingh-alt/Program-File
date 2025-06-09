# 43) Count the number of Vowel in words

word = input("Enter the sentence here: ")
vowels = "aeiou"
#word = word.casefold()
word = word.lower()
count = {}.fromkeys(vowels,0)

for char in word:
    if char in count:
        count[char]+=1
print(count)