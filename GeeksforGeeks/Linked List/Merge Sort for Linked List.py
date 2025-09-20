'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def split(self,head):
        fast = head
        slow =head
        
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
            
        #split
        second = slow.next
        slow.next = None
        return second
    def merge(self, first, second):
        if not first: 
            return second
        if not second: 
            return first
        
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            return first
        else:
            second.next = self.merge(first, second.next)
            return second
        
        
    def mergeSort(self, head):
        if not head or not head.next:
            return head
        
        second = self.split(head)
        head = self.mergeSort(head)
        second = self.mergeSort(second)
        return self.merge(head, second)
        # code here
        