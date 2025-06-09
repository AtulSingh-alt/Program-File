# 49) display Prime number using list

u = int(input("Enter the number : "))
L=[]
for n in range(2,u+1):
      if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            L.append(n)
print(L)