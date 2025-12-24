def alternateDigits(arr):
    res=[]
    for i in range(0,len(arr),2):
        res.append(arr[i])
    return res
arr=list(map(int,input().split()))
res=alternateDigits(arr)
print(res)