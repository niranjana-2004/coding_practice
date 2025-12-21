def valIndex(arr):
    res=[]
    for i in range(len(arr)):
        if arr[i]==i+1:
            res.append(arr[i])
    return res
arr=list(map(int,input().split()))
print(valIndex(arr))