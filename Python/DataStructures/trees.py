from typing import List

from DataStructures.node import BinaryTreeNode


class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def in_order_traversal(self, node: BinaryTreeNode = None, nodes: List[BinaryTreeNode] = []):
        if node is None:
            node = self.root

        if node.left:
            self.in_order_traversal(node.left, nodes)
        nodes.append(node)
        if node.right:
            self.in_order_traversal(node.right, nodes)

        return nodes

    def pre_order_traversal(self, node: BinaryTreeNode = None, nodes: List[BinaryTreeNode] = []):
        if node is None:
            node = self.root

        nodes.append(node)
        if node.left:
            self.pre_order_traversal(node.left, nodes)
        if node.right:
            self.pre_order_traversal(node.right, nodes)

        return nodes

    def post_order_traversal(self, node: BinaryTreeNode = None, nodes: List[BinaryTreeNode] = []):
        if node is None:
            node = self.root

        if node.left:
            self.post_order_traversal(node.left, nodes)
        if node.right:
            self.post_order_traversal(node.right, nodes)
        nodes.append(node)

        return nodes

    def get_height(self, node: BinaryTreeNode = None, initiated: bool = False):
        if node is None and not initiated:
            node = self.root
        elif node is None:
            return 0

        initiated = True

        left_height = self.get_height(node.left, initiated) + 1
        right_height = self.get_height(node.right, initiated) + 1
        return max(left_height, right_height)
