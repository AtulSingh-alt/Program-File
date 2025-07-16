# swapping two number by using bitwise operators

a= int(input("Enter the first value : "))
b= int(input("Enter the second value : "))
print(f"Before swapping: a = {a}, b = {b}")
# Swapping using XOR
a = a ^ b          #0101^0111 =0010 ->2
b = a ^ b          #0010^0111 =0101 ->5
a = a ^ b          #0101^0010 =0111 ->7

print(f"After swapping: a = {a}, b = {b}")