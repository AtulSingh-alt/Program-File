# Count the Number of Words and Characters

santence=input("Enter the string:")
char=0
word=1
for i in santence:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)