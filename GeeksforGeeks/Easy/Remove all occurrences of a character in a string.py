#User function Template for python3
class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here
        s = s.replace(c, '')
        return s