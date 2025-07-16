# # merge two sorted lists into one sorted list.
#
# def merge_sorted_lists(list1, list2):
#     merged_list = []
#     i, j = 0, 0
#
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1
#
#     # If there are remaining elements in list1
#     while i < len(list1):
#         merged_list.append(list1[i])
#         i += 1
#
#     # If there are remaining elements in list2
#     while j < len(list2):
#         merged_list.append(list2[j])
#         j += 1
#
#     return merged_list
#
# list1= list(map(int,input("Enter the list here :").split()))
# list2= list(map(int,input("Enter the list here :").split()))
# print(merge_sorted_lists(list1,list2))

#--------------

list1= list(map(int,input("Enter the list here :").split()))
list2= list(map(int,input("Enter the list here :").split()))
merg_list = list1 + list2

for i in range(len(merg_list)):
    for j in range(i+1,len(merg_list)):
        if merg_list[i] > merg_list[j]:
            merg_list[i],merg_list[j] = merg_list[j],merg_list[i]

print(merg_list)