#Find the largest three numbers in the list

a = list(map(int,input("Enter the number: ").split()))
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
b.append(a[len(a)-1])
b.append(a[len(a)-2])
b.append(a[len(a)-3])
print(f"The largest number are {b} in the list {a}")