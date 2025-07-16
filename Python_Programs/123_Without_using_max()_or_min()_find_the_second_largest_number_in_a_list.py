# Without using max() or min(), find the second largest number in a list
list = list(map(int,input("Enter the list here :").split()))
max = list[0]
max2 = list[0]

for num in list:
  if num > max:
      max2 = max
      max = num
  elif num > max2 and num < max:
      max2 = num

print(max2)