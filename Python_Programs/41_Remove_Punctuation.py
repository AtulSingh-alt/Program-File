# 40) Remove punctuation from a string

punc = '''!@#$%^&*()~}{|:">/<?'''
word = input("Enter the sentence here: ")
empty_str = ""

for i in word:
    if i not in punc:
        empty_str+=i
print(empty_str)
