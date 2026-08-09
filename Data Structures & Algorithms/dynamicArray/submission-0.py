class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elements = [None] * capacity
        self.last_free_index = 0; 
        self.size = 0

    def get(self, i: int) -> int:
        if i >= 0 and i <= self.capacity - 1:
            return self.elements[i]    


    def set(self, i: int, n: int) -> None:
        if i >= 0 and i <= self.capacity -1:
            self.elements[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        if self.size < self.capacity:
            self.elements[self.size] = n
            self.size = self.size + 1


    def popback(self) -> int:
        if self.size > 0:
            self.size = self.size - 1
            element_to_return = self.elements[self.size]
            self.elements[self.size] = None
            return element_to_return
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_array = [None] * self.capacity
        for i in range(len(self.elements)):
            new_array[i] = self.elements[i]
        self.elements = new_array


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
