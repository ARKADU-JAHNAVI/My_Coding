class Solution:
    def segregateEvenOdd(self, arr):
        n = len(arr)
        index = 0
        for i in range(n):
            if arr[i] % 2 == 0:
                arr[i], arr[index] = arr[index], arr[i]
                index += 1

        # sort evens and odds separately
        arr[:index] = sorted(arr[:index])
        arr[index:] = sorted(arr[index:])


''' https://www.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1  '''