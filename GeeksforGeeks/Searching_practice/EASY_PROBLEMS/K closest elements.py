class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        arr = [a for a in arr if a!=x]
        arr.sort(key=lambda a:(abs(a-x), -a))
        return arr[:k]