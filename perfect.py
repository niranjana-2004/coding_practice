def perfectArr(arr,n):
    i=1
    while(i<n and arr[i]>arr[i-1]):
        i+=1
    while(i<n and arr[i]==arr[i-1]):
        i+=1
    while(i<n and arr[i]<arr[i-1]):
        i+=1
    return(i==n)
arr=list(map(int,input().split()))
n=len(arr)
print(perfectArr(arr,n))