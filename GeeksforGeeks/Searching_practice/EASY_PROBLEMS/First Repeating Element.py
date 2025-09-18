class Solution:
    def firstRepeated(self,arr):
        # code here 
        cnt = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    return i + 1
        return -1