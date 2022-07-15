from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'{self.value}'


class LinkedListNode(Node):
    def __init__(self, value: int, next: Optional[Node] = None):
        super().__init__(value)
        self.next: Optional[LinkedListNode] = next


class DoubleLinkedListNode(Node):
    def __init__(self, value: int, next: Optional[Node] = None, previous: Optional[Node] = None):
        super().__init__(value)
        self.next: Optional[DoubleLinkedListNode] = next
        self.previous: Optional[DoubleLinkedListNode] = previous


class BinaryTreeNode(Node):
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        super().__init__(value)
        self.left: Optional[BinaryTreeNode] = left
        self.right: Optional[BinaryTreeNode] = right


class GraphNode(Node):
    def __init__(self, value: int, neighbors: Optional[List[Node]] = None, name: str = None):
        super().__init__(value)
        if neighbors is None:
            neighbors = []
        self.name = name
        self.neighbors: List[GraphNode] = neighbors

    def __repr__(self):
        return f'{self.name} ({self.value})' if self.name and self.value else f'{self.value}' if self.value else f'{self.name}'
