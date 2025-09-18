class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeLastNode(head):
        # code here
    if head is None:
        return None
    if head.next is None:
        return None
    secondlast = head
    while secondlast.next.next is not None:
        secondlast = secondlast.next
    secondlast.next = None
    return head
def printlist(head):
    while head is not None:
        print(f"{head.data} -->", end =" ")
        head = head.next 
    print("None")
if __name__ == "__main__":
    # Creating a static linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Removing the last node
    head = removeLastNode(head)

    printlist(head)       
        