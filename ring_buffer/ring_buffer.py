from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage.remove_from_head() 
            if (self.current is None) or (self.current==self.capacity):
                self.current = 0
            else:
                self.current +=1         
            
        self.storage.add_to_tail(item)
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current:
            list_buffer_contents = list_buffer_contents+[current.value]
            current = current.next
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
