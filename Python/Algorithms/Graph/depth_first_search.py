from typing import Dict, List, Optional
from DataStructures.graphs import Graph
from DataStructures.node import GraphNode


class DepthFirstSearchGeneral:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.parent: Dict[GraphNode, Optional[GraphNode]] = {}
        for start_vertex in self.graph.vertices:
            if start_vertex not in self.parent:
                self.parent[start_vertex] = None
                self.dfs_visit(start_vertex)

    def dfs_visit(self, vertex: GraphNode) -> None:
        for neighbor in self.graph.adjacency_list[vertex]:
            if neighbor not in self.parent:
                self.parent[neighbor] = vertex
                self.dfs_visit(neighbor)
