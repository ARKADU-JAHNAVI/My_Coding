class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
    
def deleteHead(head):
    if head is None:
         return None
    temp = head
    head = head.next
    temp = None
    return head
   
def printlist(curr):
    while curr is not None:
        print(curr.data, end =" ")
        if curr.next is not None:
            print("-->", end =" ")
        curr= curr.next
   
if __name__ == "__main__":

    # Create a hard-coded linked list:
    # 8 -> 2 -> 3 -> 1 -> 7
    head = Node(8)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(7)

    head = deleteHead(head)  
    printlist(head)
    
        