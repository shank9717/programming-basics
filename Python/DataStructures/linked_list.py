from DataStructures.node import Node
from DataStructures.node import LinkedListNode



class LinkedList:
    def __init__(self, root: LinkedListNode) -> None:
        self.root = root
        self.size = self.get_size()

    def get_size(self) -> int:
        current = self.root
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def find(self, value: int) -> Node:
        current = self.root
        while current:
            if current.value == value:
                return current
            current = current.next
        return -1

    def insert_first(self, value: int):
        new_node = LinkedListNode(value)
        new_node.next = self.root
        self.root = new_node
        self.size += 1
    
    def insert_last(self, value: int):
        current = self.root
        while current.next:
            current = current.next
        current.next = LinkedListNode(value)
        self.size += 1
    
    def insert_after(self, value: int, after: int):
        current = self.root
        while current:
            if current.value == after:
                next_node = current.next
                current.next = LinkedListNode(value)
                current.next.next = next_node
                self.size += 1
                return
            current = current.next
        raise ValueError(f"Value not found: {after}")
    
    def insert(self, value: int):
        self.insert_last(value)
    
    def delete_first(self):
        next_node = self.root.next
        self.root = next_node
        self.size -= 1
    
    def delete_last(self):
        current = self.root
        if current.next is None:
            self.root = None
            self.size -= 1
            return
        
        while current.next.next:
            current = current.next
        current.next = None
        self.size -= 1
    
        