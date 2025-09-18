#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        n = len(arr)
        for i in range(n):
            if arr[i] >= x:
                return i
        return -1
                
        # code here
