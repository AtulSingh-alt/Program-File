# calculate av average height

heights = input("Enter all heights separated by a space :")
height_list = heights.split()
count = 0
for height in height_list:
    count = count+1
print(count)
for i in range(count):
    height_list[i] = int(height_list[i])

total = 0
for person in height_list:
    total += person
avg = total/count
print(round(avg))