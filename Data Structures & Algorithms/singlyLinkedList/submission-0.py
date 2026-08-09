class ListNode:
    def __init__(self, new_value):
        self.value = new_value
        self.next_node = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.number_of_nodes = 0

    def get(self, index: int) -> int:
        #1st edge case where list is empty
        if self.number_of_nodes == 0:
            return -1
        #2nd edge case where index is invalid    
        if index >= self.number_of_nodes or index < 0:
            return -1    
        curr_node = self.head
        counter = 0
        if index == 0:
            return self.head.value
        while (counter != index):
            curr_node = curr_node.next_node
            counter = counter + 1
        return curr_node.value

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.number_of_nodes == 0:
            self.head = new_node
            self.tail = new_node
            self.number_of_nodes += 1
            return
        new_node.next_node = self.head
        self.head = new_node
        self.number_of_nodes += 1
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.number_of_nodes == 0:
            self.head = new_node
            self.tail = new_node
            self.number_of_nodes += 1
            return    
        self.tail.next_node = new_node
        self.tail = new_node
        self.number_of_nodes += 1

    def remove(self, index: int) -> bool:
        # 1st edge case where list is empty
        if self.number_of_nodes == 0:
            return False
        # 2nd edge case where index is invalid    
        if index >= self.number_of_nodes or index < 0:
            return False  
        # if we try to remove the head   
        if index == 0:
            self.head = self.head.next_node
            self.number_of_nodes -= 1
            if self.number_of_nodes == 0:
                self.tail = None
            return True 
        # start iteration    
        curr_node = self.head
        for i in range (index-1):
            curr_node = curr_node.next_node
        # if we try to remove the tail
        if curr_node.next_node.next_node == None:
            curr_node.next_node = None
            self.tail = curr_node
            self.number_of_nodes -= 1
            return True
        # remove somewhere in the middle
        curr_node.next_node = curr_node.next_node.next_node
        self.number_of_nodes -= 1
        return True

        
    def getValues(self) -> List[int]:
        return_array = []
        if self.number_of_nodes == 0:
            return return_array
        curr_node = self.head
        while curr_node != None:
            return_array.append(curr_node.value)
            curr_node = curr_node.next_node
        return return_array    
