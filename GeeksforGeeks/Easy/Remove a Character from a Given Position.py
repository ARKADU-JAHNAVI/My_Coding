class Solution:
    def removeCharacter(self,s, pos):
        # Remove character at index 'pos'
        return s[:pos] + s[pos+1:]
