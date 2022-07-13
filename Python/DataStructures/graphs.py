from typing import Dict, List

from DataStructures.edge import GraphEdge
from DataStructures.node import GraphNode


class Graph:
    def __init__(self, vertices: List[GraphNode] = [], edges: List[GraphEdge] = []):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list: Dict[GraphNode, List[GraphNode]] = {}
        self.update_adjacency_list()

    def add_node(self, node: GraphNode, edges: List[GraphEdge]):
        self.vertices.append(node)
        self.edges.extend(edges)
        self.update_adjacency_list()

    def add_edge(self, edge: GraphEdge):
        self.edges.append(edge)
        self.update_adjacency_list()

    def add_node(self, node: GraphNode):
        self.vertices.append(node)

    def update_adjacency_list(self):
        self.adjacency_list = {}
        for vertex in self.vertices:
            self.adjacency_list[vertex] = []
        for edge in self.edges:
            self.adjacency_list[edge.node_a].append(edge.node_b)
            if not edge.directed:
                self.adjacency_list[edge.node_b].append(edge.node_a)

    def get_edge(self, node_a: GraphNode, node_b: GraphNode):
        for edge in self.edges:
            if edge.node_a == node_a and edge.node_b == node_b:
                return edge
            if not edge.directed:
                if edge.node_a == node_b and edge.node_b == node_a:
                    return edge
        return None
