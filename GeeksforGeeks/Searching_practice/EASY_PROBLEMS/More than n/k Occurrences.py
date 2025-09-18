from collections import Counter
class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        n = len(arr)
        count = 0
        freq = Counter(arr)
        for val in freq.values():
            if val > n // k:
                count += 1
        return count
        #Your code here
