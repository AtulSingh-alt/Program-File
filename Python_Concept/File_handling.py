# Write mode user 'w'
# f1=open("File_1.txt","w")
# f1.write("Welcome to Atul's world!!!")

# Read Mode use 'r'
# f1=open("File_1.txt","r")
# print(f1.read())

# Read & write both user 'r+'
# f1=open("File_1.txt","r+")
# print(f1.tell())        #for checking the position of the cursor
# print(f1.read())
# print(f1.tell())
# f1.write("Thank you!!!")
# print(f1.tell())
# print(f1.read())
# print(f1.tell())

# Read & write both user 'w+'
# f1=open("File_1.txt","w+")
# print(f1.tell())        #for checking the position of the cursor
# f1.write("Thank you!!!")
# print(f1.tell())
# f1.write("This is Python course")
# print(f1.tell())
# f1.seek(0)              #for moving the cursor
# print(f1.tell())
# print(f1.read())
# print(f1.tell())
# f1.close()

# write the data at the end use 'a'(append)
# f1= open("File_1.txt","a")
# f1.write("Hey, Student")


# write & read the data at the end use 'a'(append)
f1= open("File_1.txt","a+")
f1.seek(0)
# f1.write("Hey, Student")
print(f1.read())