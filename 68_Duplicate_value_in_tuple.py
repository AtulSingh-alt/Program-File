# print the number of duplicate value in Tuple
num= (24,43,54,55,24,54,55)
count=0
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i] == num[j]:
            count=count+1
print(f"The number of duplicates are {count}")