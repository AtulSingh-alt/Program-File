# 47) sorting number in the list
a = list(map(int,input("Enter the number: ").split()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]

print(a)