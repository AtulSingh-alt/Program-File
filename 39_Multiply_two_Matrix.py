#38) Mulply two matrix

A = [[1,5,8],
     [4,6,7],
     [7,2,3]]
B = [[4,5,6],
     [8,9,1],
     [3,5,6]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)
