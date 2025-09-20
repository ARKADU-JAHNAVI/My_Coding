from typing import List
class Solution:
    def longestSubarray(self, arr):
        n = len(arr)
        nextgreater = [n] * n
        prevgreater = [-1] * n
        st =[]
        
        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                nextgreater[st.pop()] = i
            st.append(i)
            
        st.clear()
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] < arr[i]:
                prevgreater[st.pop()] = i
            st.append(i)
            
        maxlen = 0
        for i in range(n):
            windowsize = nextgreater[i] - prevgreater[i] - 1
            if windowsize >= arr[i]:
                maxlen = max(maxlen, windowsize)
        return maxlen