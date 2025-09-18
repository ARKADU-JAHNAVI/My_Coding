class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    @staticmethod
    def insertAtEnd(head, x):
        #code here 
        newnode = Node(x)
        if head is None:
            return newnode
            
        last = head
        while last.next is not None:
            last = last.next
        last.next = newnode
        return head
    @staticmethod
    def printlist(head):
        curr = head
        while curr is not None:
            print(curr.data, end =" ")
            if curr.next is not None:
                print("-->", end =" ")
            curr = curr.next
        print()
if __name__ == "__main__":
    # Create a linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = Node.insertAtEnd(head, 6)

    Node.printlist(head)
    
            
        