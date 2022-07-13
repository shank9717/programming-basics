from typing import List


class Node:
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f'{self.value}'


class LinkedListNode(Node):
    def __init__(self, value: int, next: Node = None):
        super().__init__(value)
        self.next: LinkedListNode = next


class DoubleLinkedListNode(Node):
    def __init__(self, value: int, next: Node = None, previous: Node = None):
        super().__init__(value)
        self.next: DoubleLinkedListNode = next
        self.previous: DoubleLinkedListNode = previous


class BinaryTreeNode(Node):
    def __init__(self, value: int, left: Node, right: Node):
        super().__init__(value)
        self.left: BinaryTreeNode = left
        self.right: BinaryTreeNode = right


class GraphNode(Node):
    def __init__(self, value: int, neighbors=None, name: str = None):
        super().__init__(value)
        if neighbors is None:
            neighbors = []
        self.name = name
        self.neighbors: List[GraphNode] = neighbors

    def __repr__(self):
        return f'{self.name} ({self.value})' if self.name and self.value else f'{self.value}' if self.value else f'{self.name}'
