'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        cnt = 0
        curr = head
        while curr is not None:
            cnt += 1
            curr = curr.next
        return cnt
        