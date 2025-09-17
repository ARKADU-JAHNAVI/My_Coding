class Solution:
    def countOnes(self, arr):
        #code here
        n = len(arr)
        cnt = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                cnt += 1
        return cnt
            