class Solution:
    def findElement(self, arr):
        for i in range(1, len(arr)-1):
            if max(arr[:i+1]) == arr[i] and min(arr[i:]) == arr[i]:
                return arr[i]
        return -1
                    
                
        # code here
        