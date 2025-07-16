# set1 = {10, 43, 42, 'Atul', True}
# print(set1)
# set2 = set()
# print(set2)
# set1.add(9)
# print(set1)
# print(len(set1))
# set1.remove(43)
# print(set1)

set1 = {'Ram', 'Shyam', 'Jenny'}
set2 = {'Jenny', 'Jiya', 'Akash'}
set3 = {'Atul', 'Sunny'}

# #For Union
# print(set1.union(set2))
# print(set1.union(('Mohan','Nikhil')))
# set1.update(set2)
# print(set1)
# #or
# #print(set1 | set2 | set3)

#For intersection
# print(set1.intersection(set2))
# #or
# print(set1 & set2)
# print(set1.intersection(set2, set3))
# print(set1.intersection(('Rahul', 'Ram')))
# set1.intersection_update(set2)
# print(set1)
# set2.intersection_update(('Mohan','Nikhil'))
# print(set2)

#For difference
# print(set1.difference(set2))
# print(set1.difference(set2,set3))
# print(set1.difference(['Bunny', 'Shyam']))
# #or
# print(set1 - set2)
#
# set1.difference_update(set2)
# print(set1)

#For Symmetric Difference
# print(set1.symmetric_difference(set2))
# #or
# print(set1 ^ set2)
# set1.symmetric_difference_update(set2)
# print(set1)
# set1.symmetric_difference_update(['Rahul', 'Krishna'])
# print(set1)

#For disjoint
# print(set1.isdisjoint(set2))
# print(set1.isdisjoint(('Ranu', 'Sardar')))

#For subset
print(set1.issubset(set2))
print(set1.issubset(('Ranu', 'Sardar', 'Ram', 'Shyam', 'Jenny')))

#For superset
print(set1.issuperset(set2))
print(set1.issuperset(('Ram', 'Shyam', 'Jenny')))

# For Clear
set3.clear()
print(set3)

# For delete
del set3
