class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


    @staticmethod
    def insertPos(head, pos, val):
        if pos < 1:
            return head
        if pos == 1:
            newnode = Node(val)
            newnode.next = head
            return newnode
        curr = head
        for i in range(1, pos-1):
            if curr is None: #list is shorter than pos-1
                return head
            curr = curr.next 
        if curr is None: # poos more than the length of list
            return head
        
        newnode  = Node(val)
        newnode.next = curr.next
        curr.next = newnode
        return head
    @staticmethod
    def printlist(head):
        curr = head
        while curr is not None:
            print(curr.data, end=" ")
            if curr.next is not None:
                print("-->", end =" ")
            curr = curr.next
        print()
if __name__ == "__main__":
    # Creating the list 1->2->4
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(4)
    
    val, pos = 3, 3
    head = Node.insertPos(head, pos, val)
    Node.printlist(head)
      