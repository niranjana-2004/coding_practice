#using sets
'''arr=list(map(int,input().split()))
result=list(set(arr))
print(result)'''

#using sets and lists
arr=list(map(int,input().split()))

seen=set()
result=[]
for num in arr:
    if num not in seen:
        seen.add(num)
        result.append(num)
print(result)