from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        close = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            left , right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(close - target):
                    close = total

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return close
                    