# Remove all duplicates from a list but preserve order
list = list(map(int,input("Enter the lsi value here: ").split()))
list2 = []
for num in list:
  if num in list2:
      continue
  else:
      list2.append(num)

print(list2)