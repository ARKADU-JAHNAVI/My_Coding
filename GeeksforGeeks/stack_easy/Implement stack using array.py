class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.capacity = n
        self.arr = [0] * self.capacity
        self.top = -1

    
    def isEmpty(self):
        # Check if stack is empty
        return self.top == -1

    
    def isFull(self):
        # Check if stack is full
        return self.top == self.capacity - 1

    
    def push(self, x):
        # Insert x at the top of the stack
        if self.top == self.capacity - 1:
            return -1
        self.top += 1
        self.arr[self.top] = x

    
    def pop(self):
        # Removes an element from the top of the stack
        if self.top == -1:
            # print("-1")
            return -1
        value = self.arr[self.top]
        self.top -= 1
        return value

    
    def peek(self):
        # Returns the top element of the stack
        if self.top == -1:
            # print("-1")
            return -1
        return self.arr[self.top]
    
    '''
    class mystack:
def __init(self, cap):
self.capacity = cap
self.arr = [0] * self.capacity
self.top = -1

def push(self, x):
if self.top = self.capacity – 1:
print(“stack overflow)
return
self.top += 1
self.arr[self.top] = x

def pop(self):
if self.top == -1:
print(“stack underflow”)
return
val = self.arr[self.top]
self.top -= 1
return val

def peek(self):	
if self.top == -1:
print(“stack is empty”)
return -1
return self.arr[self.top]

def isEmpty(self):
return self.top == -1

def isFull(self):
return self.top == self.capacity – 1
if __name__ == “__main__”:
'''