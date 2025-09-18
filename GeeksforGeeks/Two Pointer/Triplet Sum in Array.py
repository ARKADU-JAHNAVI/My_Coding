class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        n = len(arr)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j +1, n):
                    if arr[i] + arr[j] +arr[k] == target:
                        return True
        return False
    
    
    '''
    class Solution:
    def hasTripletSum(self, arr, target):
        n = len(arr)
        arr.sort()

        # Fix the first element as arr[i]
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            requiredSum = target - arr[i]

            while l < r:
                if arr[l] + arr[r] == requiredSum:
                    return True
                if arr[l] + arr[r] < requiredSum:
                    l += 1
                else:
                    r -= 1

        return False
        
        '''
