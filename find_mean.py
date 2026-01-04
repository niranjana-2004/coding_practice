def mean(arr):
    sum=0
    for i in arr:
        sum+=i
    mean=sum/len(arr)
    return mean
def median(arr):
    n=len(arr)
    arr.sort()
    res=0
    if n%2==0:
        res=(arr[n//2]+arr[(n//2)-1])//2
    else:
        res=arr[n//2]
    return res
arr=list(map(int,input().split()))
print(mean(arr))
print(median(arr))