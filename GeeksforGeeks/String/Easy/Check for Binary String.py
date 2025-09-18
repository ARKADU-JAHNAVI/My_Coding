# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        #code here
        n = len(s)
        for i in range(n):
            if s[i] != '0' and s[i] != '1':
                # i += 1
                return False
        return True