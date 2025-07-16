# Print all numbers between 1 to 100 that are divisible by both 3 and 5 but not 30
for i in range(101):
  if i % 3 == 0 and i % 5 == 0:
      if i % 30 != 0:
          print(i)