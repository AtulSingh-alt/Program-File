# Count the number of Occurrence of a character in String
def count_char(string,char):
    count=0
    for i in string:
        if i == char:
            count = count + 1
    return (f"The number of characters are: {count}")

string = input("Enter the word here: ")
char = input("Enter the character here: ")
print(count_char(string,char))