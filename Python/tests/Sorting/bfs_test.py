import math
import unittest
from unittest import TestCase

from Algorithms.Graph.breadth_first_search import BreadthFirstSearch
from DataStructures.edge import DirectedGraphEdge, UndirectedGraphEdge
from DataStructures.graphs import Graph
from DataStructures.node import GraphNode


class TestBFSAlgorithmDirectedGraph(TestCase):

    def setUp(self) -> None:
        self.nodes = [GraphNode(value) for value in range(1, 8)]
        self.edges = [
            DirectedGraphEdge(self.nodes[0], self.nodes[2]),
            DirectedGraphEdge(self.nodes[1], self.nodes[0]),
            DirectedGraphEdge(self.nodes[1], self.nodes[2]),
            DirectedGraphEdge(self.nodes[2], self.nodes[6]),
            DirectedGraphEdge(self.nodes[3], self.nodes[6]),
            DirectedGraphEdge(self.nodes[4], self.nodes[3]),
            DirectedGraphEdge(self.nodes[5], self.nodes[3]),
            DirectedGraphEdge(self.nodes[5], self.nodes[4]),
            DirectedGraphEdge(self.nodes[6], self.nodes[1]),
            DirectedGraphEdge(self.nodes[6], self.nodes[5])
        ]
        self.graph = Graph(self.nodes, self.edges)

    def test_bfs_direct_path(self):
        bfs = BreadthFirstSearch(self.graph, self.nodes[6], self.nodes[5])
        self.assertEqual(1, bfs.path.path_length)
        self.assertListEqual([self.nodes[6], self.nodes[5]], list(bfs.path.route))

    def test_bfs_no_path(self):
        bfs = BreadthFirstSearch(self.graph, self.nodes[6], GraphNode(100))
        self.assertEqual(math.inf, bfs.path.path_length)
        self.assertEqual(None, bfs.path.route)

    def test_bfs(self):
        bfs = BreadthFirstSearch(self.graph, self.nodes[3], self.nodes[4])
        self.assertEqual(3, bfs.path.path_length)
        self.assertListEqual([self.nodes[3], self.nodes[6], self.nodes[5], self.nodes[4]], list(bfs.path.route))


class TestBFSAlgorithmUndirectedGraph(TestCase):

    def setUp(self) -> None:
        self.nodes = [GraphNode(value) for value in range(1, 8)]
        self.edges = [
            UndirectedGraphEdge(self.nodes[0], self.nodes[2]),
            UndirectedGraphEdge(self.nodes[1], self.nodes[0]),
            UndirectedGraphEdge(self.nodes[1], self.nodes[2]),
            UndirectedGraphEdge(self.nodes[2], self.nodes[6]),
            UndirectedGraphEdge(self.nodes[3], self.nodes[6]),
            UndirectedGraphEdge(self.nodes[4], self.nodes[3]),
            UndirectedGraphEdge(self.nodes[5], self.nodes[3]),
            UndirectedGraphEdge(self.nodes[5], self.nodes[4]),
            UndirectedGraphEdge(self.nodes[6], self.nodes[1]),
            UndirectedGraphEdge(self.nodes[6], self.nodes[5])
        ]
        self.graph = Graph(self.nodes, self.edges)

    def test_bfs(self):
        bfs = BreadthFirstSearch(self.graph, self.nodes[3], self.nodes[4])
        self.assertEqual(1, bfs.path.path_length)
        self.assertListEqual([self.nodes[3], self.nodes[4]], list(bfs.path.route))


if __name__ == '__main__':
    unittest.main()
