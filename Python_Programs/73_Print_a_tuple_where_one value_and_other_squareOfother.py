# Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number

lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
list1=[]
for i in range(lower,upper+1):
    list1.append((i, i ** 2))
print(list1)

(2,3,5,6,8)