class Node:
    def __init__(self, new_value):
        self.value = new_value
        self.left = None
        self.right = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None


    def isEmpty(self) -> bool:
        if self.head == None:
            return True
        return False
        

    def append(self, value: int) -> None: # append right
        new_node = Node(value)
        if self.head == None and self.tail == None: # empty queue
            self.head = new_node
            self.tail = new_node
            return
        self.tail.right = new_node
        new_node.left = self.tail
        self.tail = new_node
            

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.head == None and self.tail == None: # empty queue
            self.head = new_node
            self.tail = new_node
            return
        new_node.right = self.head
        self.head.left = new_node
        self.head = new_node    
        

    def pop(self) -> int: # pop right
        val = None
        if self.head == None:
            return -1
        if self.head.right == None: # only 1 element in queue
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        val = self.tail.value    
        self.tail.left.right = None
        self.tail = self.tail.left
        return val

        

    def popleft(self) -> int:
        val = None
        if self.head == None:
            return -1
        if self.head.right == None: # only 1 element in queue
            val = self.head.value
            self.head = None
            self.tail = None
            return val
        val = self.head.value
        self.head.right.left = None
        self.head = self.head.right
        return val
        
