from ast import NamedExpr
from typing import List


class Node:
    def __init__(self, value: int):
        self.value = value

class LinkedListNode(Node):
    def __init__(self, value: int, next: Node=None):
        self.value = value
        self.next: LinkedListNode = next

class DoubleLinkedListNode(Node):
    def __init__(self, value: int, next: Node=None, previous: Node=None):
        self.value = value
        self.next: DoubleLinkedListNode = next
        self.previous: DoubleLinkedListNode = previous

class BinaryTreeNode(Node):
    def __init__(self, value: int, left: Node, right: Node):
        self.value = value
        self.left: BinaryTreeNode = left
        self.right: BinaryTreeNode = right

class GraphNode(Node):
    def __init__(self, value: int, neighbors: List[Node] = [], name: str=None):
        self.name = NamedExpr
        self.value = value
        self.neighbors: List[GraphNode] = neighbors