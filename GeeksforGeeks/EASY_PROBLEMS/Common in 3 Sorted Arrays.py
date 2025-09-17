#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        res = []
        hash_set1 = set(arr1)
        hash_set2 = set(arr2)
        for num in arr3:
            if num in hash_set1 and num in hash_set2:
                if not res or res[-1] != num:
                    res.append(num)
        return res if res else [-1]