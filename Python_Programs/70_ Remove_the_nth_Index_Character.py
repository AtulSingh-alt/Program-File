# Remove the nth Index Character

def remove(string, n):
    first = string[:n]
    last = string[n + 1:]
    return first + last


string =input("Enter the sring:")
n = int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))