class Solution:
    def countSum(self, arr, target):
        #code here
        n = len(arr)
        cnt = 0
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(n):
                        if arr[i] +arr[j] + arr[k] + arr[l] == target:
                            cnt += 1
        return cnt
                            