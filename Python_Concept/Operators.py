#a,b,c=7,8,9
#print(a,b,c)
from operator import is_not

#Airthmetic Operator & Comparison Operator
n,m=9,7
l=n+m
n+=2
l/=n
print(l)
n=9
print(n==9)
print(n<=6)
print(n<6)
print(n !=6)

#Logical Operator  (and, or, not)
z,x= 5,4
print(z>4 and x>5)
print(z>4 or x>5)
print(not(z))

#Bitwise Operator  (&, |, ^, ~, <<, >>)

p,q=26,26
print(p & q)
print(p | q)
print(p ^ q)
print(~p)
print(p << 2)
print(p >> 2)
print(p & q)

#Identity Operator (is , isnot)
print(p is q)
print(p is not q)
print(id (p))
print(id (q))

r=9
print(id(r))

r=7
print(id(r))
print(r is r)


#Membership Operator (in, not in)

str = "Atul"
print("l" in str)
print("UL" in str)
print("UL" not in str)
print("ul" in str)

l= [1, 10, -1, 0, 17]
print(10 in l)
print(10 not in l)
