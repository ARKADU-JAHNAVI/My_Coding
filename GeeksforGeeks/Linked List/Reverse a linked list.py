class Node:
    def __init__(self, newData):
        self.data = newData
        self.next = None
def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        nextnode = curr.next #20
        curr.next = prev    # 10.next = None
        prev = curr         # 10
        curr = nextnode     #20 came first
    return prev
def printlist(head):
    while head is not None:
        print(f"{head.data} -->", end = " ")
        head = head.next 
    print("None")

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head = reverse(head)
    printlist(head)