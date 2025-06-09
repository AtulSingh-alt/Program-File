# 39) String is Palindrome or not

word = input("Enter a word here: ")
rev = word[::-1]
if word == rev:
    print("It is Palindrome word")
else:
    print("It is not a Palindrome word")
