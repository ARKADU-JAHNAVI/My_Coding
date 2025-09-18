class Solution:
    def getThreeLargest(self, arr):
        # code here
        n = len(arr)
        res = []
        fst = sec = thd = float('-inf')
        for i in range(n):
            if arr[i] > fst:
                thd =sec
                sec = fst
                fst = arr[i]
            elif arr[i] > sec and arr[i] != fst:
                thd = sec
                sec = arr[i]
            elif arr[i] > thd and arr[i] != fst and arr[i] != sec:
                thd = arr[i]
        if fst == float('-inf'):
            return res
        res.append(fst)
        if sec == float('-inf'):
            return res
        res.append(sec)
        if thd == float('-inf'):
            return res
        res.append(thd)
        
        return res
        