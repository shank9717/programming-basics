from typing import Dict, List
from DataStructures.graphs import Graph
from DataStructures.node import GraphNode


class BreadthFirstSearch:
    def __init__(self, graph: Graph, start_vertex: GraphNode, target_vertext: GraphNode):
        self.graph = graph
        self.visited: Dict[GraphNode, bool] = {}
        self.queue: List[GraphNode] = []
        self.level: Dict[GraphNode, int] = {}
        self.parent: Dict[GraphNode: int] = {}
        self.bfs(start_vertex, target_vertext)
    
    def bfs(self, start_vertex: GraphNode, target_vertext: GraphNode):
        self.bfs_visit(start_vertex, target_vertext)
    
    def bfs_visit(self, start_vertex: GraphNode, target_vertext: GraphNode):
        self.visited[start_vertex] = True
        self.queue.append(start_vertex)
        current_level = 0
        while self.queue:
            current_vertex = self.queue.pop(0)
            for neighbor in self.graph.adjecency_list[current_vertex]:
                if neighbor.value == target_vertext.value:
                    self.visited[neighbor] = True
                    self.parent[neighbor] = current_vertex
                    self.level[neighbor] = current_level
                    return
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.level[neighbor] = current_level
                    self.parent[neighbor] = current_vertex
                    self.queue.append(neighbor)
            current_level += 1

class BreadthFirstSearchGeneral:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited: Dict[GraphNode, bool] = {}
        self.queue: List[GraphNode] = []
        self.level: Dict[GraphNode, int] = {}
        self.parent: Dict[GraphNode: int] = {}
        self.bfs()
    
    def bfs(self):
        for start_vertex in self.graph.vertices:
            if start_vertex not in self.visited:
                self.bfs_visit(start_vertex)
    
    def bfs_visit(self, start_vertex: GraphNode):
        self.visited[start_vertex] = True
        self.queue.append(start_vertex)
        current_level = 0
        while self.queue:
            current_vertex = self.queue.pop(0)
            for neighbor in self.graph.adjecency_list[current_vertex]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.level[neighbor] = current_level
                    self.parent[neighbor] = current_vertex
                    self.queue.append(neighbor)
            current_level += 1
    