#User function Template for python3

class Solution:
    #Complete the below function
    def minOps(self,arr, x):
        n = len(arr)
        max1 = max(arr)
        res = 0
        for i in range(n):
            if ((max1 - arr[i]) % x != 0):
                return -1
            else:
                res += (max1 - arr[i]) // x
        return res
        #Your code here