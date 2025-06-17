s = input("Enter the sentence here: ")
words, word = [], ''

for ch in s:
    if ch != ' ':
        word += ch
    elif word:
        words.append(word)
        word = ''
if word:
    words.append(word)

reversed_string = ''
for i in range(len(words) - 1, -1, -1):
    reversed_string += words[i]
    if i != 0:
        reversed_string += ' '

print(reversed_string)