class Solution:
    def remDuplicate(self, arr):
        # code here 
        n = len(arr)
        res = []
        for i in range(n):
            if arr[i] not in res:
                res.append(arr[i])
        return res

''' class Solution:
    def remDuplicate(self, arr):
        seen = set()
        a = []
        for num in arr:
            if num not in seen:
                a.append(num)
                seen.add(num)
        return a  '''