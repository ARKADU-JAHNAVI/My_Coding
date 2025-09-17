class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        total = n * (n+1) // 2
        repeating = -1
        unique = set()
        for i in range(0, n):
            if arr[i] in unique:
                repeated = arr[i]
                break
            else:
                unique.add(arr[i])
        return [repeated, int(total - (sum(arr) - repeated))]

