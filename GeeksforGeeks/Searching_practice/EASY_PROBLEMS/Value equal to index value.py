#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        res = []
        n = len(arr)
        for i in range(n):
            if arr[i] == i+1:
                res.append(i+1)
        return res
                