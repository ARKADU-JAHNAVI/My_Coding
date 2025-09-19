class Solution:
    def removeDuplicates(self, arr):
        # code here 
        n = len(arr)
        arr.sort()
        res =[]
        seen =set()
        for num in arr:
            if num not in res:
                res.append(num)
                seen.add(num)
        return res