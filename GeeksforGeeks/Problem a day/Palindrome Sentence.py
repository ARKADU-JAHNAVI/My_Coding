import re
class Solution:
    def isPalinSent(self, s):
        # code here
        s = s.replace(" ","")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        if s != s[::-1]:
            return False
        return True
