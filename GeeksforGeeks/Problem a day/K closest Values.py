'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
import heapq 
from collections import deque
class Solution:
    def getKClosest(self, root, target, k):
        # code here
        queue=deque([root])
        heap=[]
        while queue:
            node=queue.popleft()
            dist=abs(node.data-target)
            heapq.heappush(heap,(-dist,-node.data))
            if len(heap)>k:
                heapq.heappop(heap)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res=[-val for key,val in heap]
        return res
        
    