from typing import List
class Solution:
    def twoSum(self, arr, target):
        l = 0
        h = len(arr) - 1
        while l <h:
            sum = arr[l] + arr[h]
            if sum  == target:
                return [l+1, h+1]
            elif sum < target:
                l += 1
            else:
                h -=1
        return [-1, -1]
