# Swap the first and last elements of a list (without using temp variable)
list = list(map(int,input("Enter the list here :").split()))

list[0],list[len(list)-1] = list[len(list)-1], list[0]
print(list)