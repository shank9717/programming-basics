from typing import List, Dict

from DataStructures.node import BinaryTreeNode


class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root

    def in_order_traversal(self, node: BinaryTreeNode = None, nodes: List[BinaryTreeNode] = []) -> List[BinaryTreeNode]:
        if node is None:
            node = self.root

        if node.left:
            self.in_order_traversal(node.left, nodes)
        nodes.append(node)
        if node.right:
            self.in_order_traversal(node.right, nodes)

        return nodes

    def pre_order_traversal(self, node: BinaryTreeNode = None, nodes: List[BinaryTreeNode] = []) -> \
            List[BinaryTreeNode]:
        if node is None:
            node = self.root

        nodes.append(node)
        if node.left:
            self.pre_order_traversal(node.left, nodes)
        if node.right:
            self.pre_order_traversal(node.right, nodes)

        return nodes

    def post_order_traversal(self, node: BinaryTreeNode = None, nodes: List[BinaryTreeNode] = []) -> \
            List[BinaryTreeNode]:
        if node is None:
            node = self.root

        if node.left:
            self.post_order_traversal(node.left, nodes)
        if node.right:
            self.post_order_traversal(node.right, nodes)
        nodes.append(node)

        return nodes

    def level_order_traversal_helper(self, node: BinaryTreeNode, current_level: int, levels: List[int],
                                     level_nodes: Dict[int, List[BinaryTreeNode]]) -> List[int]:

        if current_level in level_nodes:
            level_nodes[current_level].append(node)
        else:
            level_nodes[current_level] = [node]
        if not current_level in levels:
            levels.append(current_level)

        if node.left is not None:
            self.level_order_traversal_helper(node.left, current_level + 1, levels, level_nodes)
        if node.right is not None:
            self.level_order_traversal_helper(node.right, current_level + 1, levels, level_nodes)

        return levels

    def level_order_traversal(self, node: BinaryTreeNode = None, nodes: List[BinaryTreeNode] = []) -> \
            List[BinaryTreeNode]:
        if node is None:
            node = self.root

        current_level = 0
        level_nodes = {}

        levels = self.level_order_traversal_helper(node, current_level, [], level_nodes)

        for level in range(max(levels) + 1):
            nodes.extend(level_nodes[level])

        return nodes

    def left_view(self, node: BinaryTreeNode = None) -> List[BinaryTreeNode]:
        if node is None:
            node = self.root

        nodes: List[BinaryTreeNode] = []
        current_level = 0
        level_nodes = {}

        levels = self.level_order_traversal_helper(node, current_level, [], level_nodes)

        for level in range(max(levels) + 1):
            nodes.append(level_nodes[level][0])

        return nodes

    def get_height(self, node: BinaryTreeNode = None, initiated: bool = False) -> int:
        if node is None and not initiated:
            node = self.root
        elif node is None:
            return 0

        initiated = True

        left_height = self.get_height(node.left, initiated) + 1
        right_height = self.get_height(node.right, initiated) + 1
        return max(left_height, right_height)
