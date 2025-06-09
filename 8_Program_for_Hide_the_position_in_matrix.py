# // How to hide the position in matrix

row1 = input("Enter the value in list format : ")
row2 = input("Enter the value in list format : ")
row3 = input("Enter the value in list format : ")
matrix = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position= input("Enter the position where you want to hide : ")
row_number = int (position[0])
column_number = int(position[1])
row_selected = matrix[row_number-1]
row_selected[column_number-1] = 'x'
print(f"{row1}\n{row2}\n{row3}")