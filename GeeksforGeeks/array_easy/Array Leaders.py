class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        res =[]
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] < arr[j]:
                    break
            else:
                res.append(arr[i])
        return res