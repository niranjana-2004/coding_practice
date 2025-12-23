def arrMultiply(arr):
    epdt=1
    opdt=1
    for i in range(len(arr)):
        if i%2==0:
            epdt*=arr[i]
        else:
            opdt*=arr[i]
    return epdt,opdt
arr=list(map(int,input().split()))
print(arrMultiply(arr))