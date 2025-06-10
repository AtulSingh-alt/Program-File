# Print even and odd number in separated list
n=list(map(int,input("Enter number:").split()))
even =[]
odd =[]
for i in range(len(n)):
    if n[i]%2 ==0:
        even.append(n[i])
#        print(even)
    else:
        odd.append(n[i])
#       print(odd)
print(f"The given numbers are {n}\nThe even numbers are {even}\nThe odd numbers are {odd}")