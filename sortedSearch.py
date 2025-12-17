class Solution:
    def sortedSearch(self,arr,key):
        for i in range(len(arr)):
            if arr[i]==key:
                return True
        return False
arr=list(map(int,input().split()))
key=int(input())
obj=Solution()
print(obj.sortedSearch(arr,key))