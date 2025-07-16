# Concatenate two Lists while replacing duplicate values
l1= [3,4,6,"a","u"]
l2= [3,5,"g","j","i"]

l = list(set(l1+l2))
print(l)
