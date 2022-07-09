from typing import Dict, List
from DataStructures.graphs import Graph
from DataStructures.node import GraphNode


class DepthFirstSearchGeneral:
    def __init__(self, graph: Graph, start_vertex: GraphNode):
        self.graph = graph
        self.parent: Dict[GraphNode: int] = {}
        for start_vertex in self.graph.vertices:
            if start_vertex not in self.parent:
                self.parent[start_vertex] = None
                self.dfs_visit(start_vertex)

    def dfs_visit(self, vertex: GraphNode):
        for neighbor in self.graph.adjecency_list[vertex]:
            if neighbor not in self.parent:
                self.parent[neighbor] = vertex
                self.dfs_visit(neighbor)
    
    