# Calculate an average of list's elements

n=list(map(int,input("Enter the number : ").split()))
avg = sum(n) / len(n)
print("Average of elements in the list",round(avg,2))