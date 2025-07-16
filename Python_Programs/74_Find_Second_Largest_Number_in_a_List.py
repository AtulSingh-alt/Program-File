# Find Second Largest Number in a List

num =list(map(int,input("Enter the number in the list here: ").split()))
val=[]
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i]>num[j]:
            num[i],num[j] = num[j],num[i]
val.append(num[len(num)-2])
print(val)