class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self,X):
        self.s1.append(X)
        # code here
    def dequeue(self):
        # code here
        if not self.s1 and not self.s2:
            return -1
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()