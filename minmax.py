arr=list(map(int,input().split()))
min=arr[0]
max=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
    if arr[i]>max:
        max=arr[i]
print(max,min)