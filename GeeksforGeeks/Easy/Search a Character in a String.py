#User function Template for python3
class Solution:
    
    # Function to search for a character in the string
    def searchCharacter(self, s, ch):
        # code here
        n = len(s)
        for i in range(n):
            if s[i] == ch:
                return i
        return -1
        
            