from typing import Dict, List
from DataStructures.node import GraphNode
from DataStructures.edge import GraphEdge


class Graph:
    def __init__(self, vertices: List[GraphNode] = [], edges: List[GraphEdge] = []):
        self.vertices = vertices
        self.edges = edges
        self.update_adjecency_list()
    
    def add_node(self, node: GraphNode, edges: List[GraphEdge]):
        self.vertices.append(node)
        self.edges.extend(edges)
        self.update_adjecency_list()
    
    def add_edge(self, edge: GraphEdge):
        self.edges.append(edge)
        self.update_adjecency_list()

    def update_adjecency_list(self):
        self.adjecency_list: Dict[GraphNode, List[GraphNode]] = {}
        for vertex in self.vertices:
            self.adjecency_list[vertex] = []
        for edge in self.edges:
            self.adjecency_list[edge.node_a].append(edge.node_b)
            self.adjecency_list[edge.node_b].append(edge.node_a)

class UndirectedGraph(Graph):
    pass