import unittest
from unittest import TestCase

from Algorithms.Graph.dijkstra import Dijkstra
from DataStructures.edge import DirectedGraphEdgeWeighted
from DataStructures.graphs import Graph
from DataStructures.node import GraphNode


class TestBFSAlgorithmDirectedGraph(TestCase):

    def setUp(self) -> None:
        self.nodes = [GraphNode(value, name=chr(value + 64)) for value in range(1, 6)]
        self.edges = [
            DirectedGraphEdgeWeighted(self.nodes[0], self.nodes[1], 10),
            DirectedGraphEdgeWeighted(self.nodes[0], self.nodes[2], 3),
            DirectedGraphEdgeWeighted(self.nodes[1], self.nodes[2], 1),
            DirectedGraphEdgeWeighted(self.nodes[2], self.nodes[1], 4),
            DirectedGraphEdgeWeighted(self.nodes[1], self.nodes[3], 2),
            DirectedGraphEdgeWeighted(self.nodes[2], self.nodes[3], 8),
            DirectedGraphEdgeWeighted(self.nodes[2], self.nodes[4], 2),
            DirectedGraphEdgeWeighted(self.nodes[3], self.nodes[4], 7),
            DirectedGraphEdgeWeighted(self.nodes[4], self.nodes[3], 9)
        ]
        self.graph = Graph(self.nodes, self.edges)

    def test_dijkstra_start_node_a(self):
        dijkstra = Dijkstra(self.graph, self.nodes[0])

        path_to_a = dijkstra.find_path(self.nodes[0])
        self.assertEqual(0, path_to_a.path_length)
        self.assertListEqual([self.nodes[0]], list(path_to_a.route))

        path_to_b = dijkstra.find_path(self.nodes[1])
        self.assertEqual(7, path_to_b.path_length)
        self.assertListEqual([self.nodes[0], self.nodes[2], self.nodes[1]], list(path_to_b.route))

        path_to_c = dijkstra.find_path(self.nodes[2])
        self.assertEqual(3, path_to_c.path_length)
        self.assertListEqual([self.nodes[0], self.nodes[2]], list(path_to_c.route))

        path_to_d = dijkstra.find_path(self.nodes[3])
        self.assertEqual(9, path_to_d.path_length)
        self.assertListEqual([self.nodes[0], self.nodes[2], self.nodes[1], self.nodes[3]], list(path_to_d.route))

        path_to_e = dijkstra.find_path(self.nodes[4])
        self.assertEqual(5, path_to_e.path_length)
        self.assertListEqual([self.nodes[0], self.nodes[2], self.nodes[4]], list(path_to_e.route))


if __name__ == '__main__':
    unittest.main()
