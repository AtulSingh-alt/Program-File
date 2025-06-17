s = input("Enter the sentence here: ")
words = s.split()
reversed_string = ''

for i in range(len(words) - 1, -1, -1):
    reversed_string += words[i]
    if i != 0:
        reversed_string += ' '

print(reversed_string)