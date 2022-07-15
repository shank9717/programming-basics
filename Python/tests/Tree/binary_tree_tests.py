import unittest
from typing import List
from unittest import TestCase

from DataStructures.node import BinaryTreeNode
from DataStructures.trees import BinaryTree


class TestSearchingAlgorithms(TestCase):

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

if __name__ == '__main__':
    unittest.main()
