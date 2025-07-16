numbers = [10, 0, -4, 9, 7]
name = ["At", "Atul", "Singh"]
mix_list = [3, "AT", -4, "Singh"]

print(numbers,'\n',name,'\n',mix_list)
print(len(numbers))
print(numbers[1:])
print(numbers[0:3])
print(numbers[:3])
print(numbers[0:3:2])
print(numbers[0:5:3])

#for sorting
numbers.sort()
print(numbers)

#for Reversing
numbers.reverse()
print(numbers)

#for max & min
print(max(numbers))
print(min(numbers))

#for adding the value
numbers.append(13)
print(numbers)

#for adding the value at particular position
numbers.insert(1,17)
print(numbers)

#for adding multiple value in the list
numbers.extend([90,89,30])
print(numbers)

#for replacing value in the list
numbers[1] = 61
print(numbers)

numbers[1:4] = 65,72,83
print(numbers)

#for removing the value from the list
numbers.remove(0)
print(numbers)

#for removing the value from the list by index
numbers.pop(1)
print(numbers)

#for counting the particular value from the list
print(numbers.count(90))