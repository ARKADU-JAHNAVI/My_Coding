'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def printList(self, head):
        # code here
        curr = head
        res = []
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res
            