class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n = len(arr)
        if n < k:
            return -1
        
        win = sum(arr[:k])
        maxsum = win
        
        for i in range(n-k):
            win = win - arr[i] + arr[i+k]
            maxsum = max(win, maxsum)
        return maxsum