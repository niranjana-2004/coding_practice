def sumMatrix(n,m,mat):
    sum=0
    for i in range(n):
        for j in range(m):
            sum+=mat[i][j]
    return sum
mat=[[4,5,6],
     [3,4,5]]
n=len(mat)
m=len(mat[0])
print(sumMatrix(n,m,mat))