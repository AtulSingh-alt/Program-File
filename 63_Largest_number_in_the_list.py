# Find the largest number in the list

a = list(map(int,input("Enter the number in the list").split()))
max = a[0]
for i in range(len(a)):
    if a[i]>max:
        max = a[i]
print(f"The largest number is {max} in the list of {a}")
