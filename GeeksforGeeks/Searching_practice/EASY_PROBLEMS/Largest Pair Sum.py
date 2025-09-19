
from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        n = len(arr)
        maxsum = float('-inf')
        for i in range(n-1):
            for j in range(i+1,n):
                sum = arr[i] + arr[j]
                if sum > maxsum:
                    maxsum = sum
        return -1 if maxsum == float('-inf') else maxsum
                    
        # code here
        
