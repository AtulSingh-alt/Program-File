# Count how many times the digit 7 appears from 1 to N
n = int(input("Enter the number here :"))
count = 0
for i in range(1, n+1):
    temp = str(i)
    for char in temp:
        if int(char) == 7:
            count += 1

print(count)