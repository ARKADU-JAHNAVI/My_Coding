#User function Template for python3
class Solution:
    def threeSum(self, arr, target):
        # Your code here
        n = len(arr)
        res = []
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if arr[i] + arr[j] + arr[k] == target:
                        curr = sorted([arr[i], arr[j], arr[k]])
                        if curr not in res:
                            res.append(curr)
        return res
                    