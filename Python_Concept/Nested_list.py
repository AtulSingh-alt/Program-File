#list1 = [10,27,92,[9,22,88],92,90]
#print(len(list1))
#print(list1[3][0])
#print(list1[-3])
#print(list1[len(list1)-2])
#print(list1[3][0:3:2])

#list2 = [10, 34, 90, ['Mohan', 'Shyam', 'Ram'], 89]
#lenght = len(list2)
#print(lenght)
#print(list2[3][2])


#Nested list program

row1 = [10, 13, 19]
row2 = [21, 24, 28]
row3 = [31, 33, 37]

matrix = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Enter the position where you want to hide money: ")
#32
row_number = int(position[0])
column_number = int(position[1])
row_selected = matrix[row_number - 1]
row_selected[column_number -1] = 'x'
print(f"{row1}\n{row2}\n{row3}")