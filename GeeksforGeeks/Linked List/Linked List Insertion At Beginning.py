class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        
    @staticmethod
    def insertAtFront(head, x):
        #code here
        newnode = Node(x)
        newnode.next = head
        return newnode
    @staticmethod
    def printlist(head):
        curr = head
        while curr is not None:
            print(curr.data, end =" ")
            if curr.next is not None:
                print('-->', end =" ")
            curr = curr.next
        print()

if __name__ == "__main__":
    # Create the linked list 2->3->4->5
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    
    x = 1
    head = Node.insertAtFront(head, x)
    
    Node.printlist(head)
        
        
