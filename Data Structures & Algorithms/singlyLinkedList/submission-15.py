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
        if self.number_of_nodes == 0 or index >= self.number_of_nodes or index < 0 : # empty or out of bound
            return -1
        if index == self.number_of_nodes - 1: # handles case when returning first and last element
            return self.tail.value

        iterator = 0
        current_node = self.head
        while iterator < self.number_of_nodes:
            if iterator == index:
                return current_node.value
            current_node = current_node.next_node
            iterator += 1
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.number_of_nodes == 0: # empty list case
            self.head = new_node
            self.tail = new_node
            self.number_of_nodes += 1
            return
        new_node.next_node = self.head
        self.head = new_node    
        self.number_of_nodes += 1
    
    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.number_of_nodes == 0: # empty list case
            self.head= new_node
            self.tail = new_node
            self.number_of_nodes += 1
            return
        self.tail.next_node = new_node
        self.tail = new_node    
        self.number_of_nodes += 1

    def remove(self, index: int) -> bool:
        if self.number_of_nodes == 0 or index >= self.number_of_nodes or index < 0: # empty or out of bound
            return False
        # handle head case
        if index == 0:
            if self.number_of_nodes == 1:
                self.head = None
                self.tail = None
                self.number_of_nodes -= 1
                return True
            self.head = self.head.next_node
            self.number_of_nodes -= 1
            return True        
                
        iterator = 0
        current_node = self.head
        while iterator < self.number_of_nodes:
            if iterator + 1 == index:
                if index == self.number_of_nodes - 1: # handle tail case
                    self.tail = current_node
                current_node.next_node = current_node.next_node.next_node
                self.number_of_nodes -= 1
                return True
            current_node = current_node.next_node    
            iterator += 1    

    
    def getValues(self) -> List [int]:
        iterator = 0
        values_list = []
        current_node = self.head
        while iterator < self.number_of_nodes:
            values_list.append(current_node.value)
            iterator += 1
            current_node = current_node.next_node
        return values_list