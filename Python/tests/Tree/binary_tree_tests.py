import unittest
from unittest import TestCase

from DataStructures.node import BinaryTreeNode
from DataStructures.trees import BinaryTree


class TestTreeTraversalAlgorithms(TestCase):

    def setUp(self) -> None:
        root = BinaryTreeNode(15)
        root.left = BinaryTreeNode(24)
        root.right = BinaryTreeNode(54)
        root.left.left = BinaryTreeNode(35)
        root.right.left = BinaryTreeNode(62)
        root.right.right = BinaryTreeNode(13)
        self.binary_tree = BinaryTree(root)

    def test_in_order_traversal(self):
        in_order_nodes = self.binary_tree.in_order_traversal()
        self.assertListEqual([35, 24, 15, 62, 54, 13], [node.value for node in in_order_nodes])

    def test_pre_order_traversal(self):
        in_order_nodes = self.binary_tree.pre_order_traversal()
        self.assertListEqual([15, 24, 35, 54, 62, 13], [node.value for node in in_order_nodes])

    def test_post_order_traversal(self):
        in_order_nodes = self.binary_tree.post_order_traversal()
        self.assertListEqual([35, 24, 62, 13, 54, 15], [node.value for node in in_order_nodes])

    def test_level_order_traversal(self):
        level_order_nodes = self.binary_tree.level_order_traversal()
        self.assertListEqual([15, 24, 54, 35, 62, 13], [node.value for node in level_order_nodes])

    def test_get_height(self):
        height = self.binary_tree.get_height()
        self.assertEqual(height, 3)

        binary_tree = BinaryTree(BinaryTreeNode(10))
        height = binary_tree.get_height()
        self.assertEqual(height, 1)

        node = BinaryTreeNode(10)
        node.left = BinaryTreeNode(0)
        binary_tree = BinaryTree(node)
        height = binary_tree.get_height()
        self.assertEqual(height, 2)


class TestLeftView(TestCase):

    def test_left_view_case_one(self):
        node = BinaryTreeNode(1)
        node.left = BinaryTreeNode(2)
        node.right = BinaryTreeNode(3)
        node.left.left = BinaryTreeNode(4)
        node.left.right = BinaryTreeNode(5)
        node.right.right = BinaryTreeNode(6)
        node.right.right.right = BinaryTreeNode(7)

        left_view_nodes = BinaryTree(node).left_view()
        left_view_nodes = [node.value for node in left_view_nodes]
        self.assertListEqual([1, 2, 4, 7], left_view_nodes)

    def test_left_view_case_two(self):
        node = BinaryTreeNode(1)
        node.left = BinaryTreeNode(2)
        node.right = BinaryTreeNode(3)
        node.left.right = BinaryTreeNode(4)
        node.left.right.right = BinaryTreeNode(5)
        node.left.right.right.right = BinaryTreeNode(6)
        left_view_nodes = BinaryTree(node).left_view()
        left_view_nodes = [node.value for node in left_view_nodes]
        self.assertListEqual([1, 2, 4, 5, 6], left_view_nodes)


if __name__ == '__main__':
    unittest.main()
