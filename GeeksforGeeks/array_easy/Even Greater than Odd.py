#User function Template for python3

class Solution:
    def rearrangeArray(self, arr):
        # code here
        n = len(arr)
        for i in range(1, n):
            if (i + 1) % 2 == 0:
                if arr[i] < arr[i-1]:
                    arr[i] , arr[i-1] = arr[i-1], arr[i]
            else:
                if arr[i] > arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
        return arr
    