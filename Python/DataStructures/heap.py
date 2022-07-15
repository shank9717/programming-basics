from typing import List
from DataStructures.node import BinaryTreeNode

class Heap:
    def __init__(self, array: List):
        self.array = array
        self.heap_size = len(array)

    def generate_tree(self, array: List) -> BinaryTreeNode:
        main_node = BinaryTreeNode(array[0], None, None)
        for idx in range(1, len(array)):
            node = BinaryTreeNode(array[idx], None, None)
            self._insert_node(main_node, node)
        return main_node

    def insert(self, num: int):
        # Add num to array
        self.array.append(num)
        self.heap_size += 1
    
    def extract(self):
        num = self.array[0]
        self.array.remove(num)
        self.heap_size -= 1
        return num
    
    def _insert_node(self, main_node: BinaryTreeNode, node: BinaryTreeNode) -> bool:
        if main_node.left is None:
            main_node.left = node
            return True
        elif main_node.right is None:
            main_node.right = node
            return True
        elif self._insert_node(main_node.left, node):
            return True
        else:
            self._insert_node(main_node.right, node)
    
    def __repr__(self) -> str:
        return str(self.array)
    

class MaxHeap(Heap):
    def build_max_heap(self) -> None:
        # This would be nLog(n) time due to the for-loop, but essentially it is much faster since max_heapify does log(N) work only for top node.
        for idx in range(self.heap_size // 2 - 1, -1, -1):
            self.max_heapify(idx)

    def max_heapify(self, idx: int) -> None:
        # This step would be log(n) time since it is called from build_max_heap() and it turns out that the children are already max heaps
        if idx < self.heap_size:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            largest_idx = idx
            if left_idx < self.heap_size and self.array[left_idx] > self.array[idx]:
                largest_idx = left_idx
            if right_idx < self.heap_size and self.array[right_idx] > self.array[largest_idx]:
                largest_idx = right_idx

            if largest_idx != idx:
                self.array[idx], self.array[largest_idx] = self.array[largest_idx], self.array[idx]
                self.max_heapify(largest_idx)

    def insert(self, num) -> None:
        # This would be log(N) time
        self.insert(num)
        self.max_heapify(0)
    
    def max(self):
        return self.array[0]
    
    def extract(self):
        return self.extract_max()

    def extract_max(self):
        max_num = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.array.pop()
        self.heap_size -= 1
        self.max_heapify(0)
        return max_num
    
class MinHeap(Heap):
    def build_min_heap(self) -> None:
        # This would be nLog(n) time due to the for-loop, but essentially it is much faster since max_heapify does log(N) work only for top node.
        for idx in range(self.heap_size // 2 - 1, -1, -1):
            self.min_heapify(idx)

    def min_heapify(self, idx: int) -> None:
        # This step would be log(n) time since it is called from build_max_heap() and it turns out that the children are already max heaps
        if idx < self.heap_size:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            smallest_idx = idx
            if left_idx < self.heap_size and self.array[left_idx] < self.array[idx]:
                smallest_idx = left_idx
            if right_idx < self.heap_size and self.array[right_idx] < self.array[smallest_idx]:
                smallest_idx = right_idx

            if smallest_idx != idx:
                self.array[idx], self.array[smallest_idx] = self.array[smallest_idx], self.array[idx]
                self.min_heapify(smallest_idx)

    def insert(self, num) -> None:
        # This would be log(N) time
        self.insert(num)
        self.min_heapify(0)
    
    def min(self):
        return self.array[0]
    
    def extract_min(self):
        max_num = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.array.pop()
        self.heap_size -= 1
        self.min_heapify(0)
        return max_num
    
    def extract(self):
        return self.extract_min()