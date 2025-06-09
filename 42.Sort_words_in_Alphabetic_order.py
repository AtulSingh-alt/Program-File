# 41) Sort words  in Alphabetic order

word = input("Enter the sentence here: ")
spt = word.split()
for i in range(len(spt)):
    spt[i] = spt[i].lower()
spt.sort()
print(spt)
#or
for i in spt:
    print(i)
