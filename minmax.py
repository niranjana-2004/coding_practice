class Solution:
    def getMinMax(self,arr):
        minimum=arr[0]
        maximum=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>maximum:
                maximum=arr[i]
            if arr[i]<minimum:
                minimum=arr[i]
        return maximum,minimum
arr=list(map(int,input().split()))
obj=Solution()
res=obj.getMinMax(arr)
print(res)