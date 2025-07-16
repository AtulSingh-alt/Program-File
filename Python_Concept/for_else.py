# tuple1 = (2,34,5,-1,8)
# for i in tuple1:
#     print(i)
# else:
#     print("Loop successfully completed and we are in else block now !!!")
from itertools import count

# when loop has not successfully executed, else will not get execute
#
# tuple1 = (2,34,5,-1,8)
# for i in tuple1:
#     print(i)
#     if i == 5:
#         break
# else:
#     print("Loop successfully completed and we are in else block now !!!")
#

# calculate av average height

# heights = input("Enter all heights separated by a space :")
# height_list = heights.split()
# count = 0
# for height in height_list:
#     count = count+1
# print(count)
# for i in range(count):
#     height_list[i] = int(height_list[i])
#
# total = 0
# for person in height_list:
#     total += person
# avg = total/count
# print(round(avg))


# find the max number in the list
number = input("Enter the list number :")
number_list = number.split()
count = 0
for number in number_list:
    count+=1
print(f"The length of teh list is : {count}")
for i in range(0, count):
    number_list[i] = int(number_list[i])
maximum_number = number_list[0]
for number in number_list:
    if number > maximum_number:
        maximum_number = number
print(f"The maximum number is : {maximum_number}")
