class Solution:

    def findMaximum(self, arr):
        maximum = arr[0]  # use a safe variable name
        for i in range(len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
        return maximum
