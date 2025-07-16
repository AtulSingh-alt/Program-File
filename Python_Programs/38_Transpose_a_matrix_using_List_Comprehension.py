# 37) or Transpose a Matrix (rows become column & column bacome rows) using List Comprehension

A = [[1,2,3],
     [4,5,6]]
T = [[A[j][i] for j in range(len(A))] for i in range (len(A[0]))]
for i in T:
    print(i)