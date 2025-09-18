#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        # code here
        low , high = 0, len(arr) - 1
        while low < high:
            if arr[low] == 1:
                if arr[high] != 1:
                    arr[low], arr[high] = arr[high], arr[low]
                    high -= 1
                    low += 1
                else:
                    high -= 1
            else:
                low += 1
                
