tuple1 = (12, 4, -6, "Atul", True )
tuple2 = (45, 47, 90)
tuple3 = (tuple1, tuple2)
tuple4 = tuple1 + tuple2
tuple5 = (10,)*5
print(tuple1)
print(tuple1[1])
print(tuple1[-1])
print(type(tuple1))
print(tuple1[1:4])
print(tuple1[:4])
print(tuple1[::2])
print(tuple3)
print(tuple3[1])
print(len(tuple3))
print(tuple4)
print(max(tuple2))
print(min(tuple2))
print(tuple1.count(12))
print(tuple1.index(12))
list1 = [3,4,5,8]
print(tuple(list1))
print(tuple5)