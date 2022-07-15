import math
from collections import deque
from typing import Dict, List, Tuple

from DataStructures.graphs import Graph
from DataStructures.node import GraphNode


class BreadthFirstSearch:
    class Path:
        def __init__(self, route: Tuple[GraphNode] = None, path_length: int = math.inf):
            self.route = route
            self.path_length = path_length

        @staticmethod
        def calculate_path(parents: Dict[GraphNode, GraphNode], start_vertex: GraphNode, target_vertex: GraphNode):
            path = BreadthFirstSearch.Path()
            route = deque()
            current_vertex = target_vertex
            route.appendleft(current_vertex)
            while current_vertex in parents:
                current_vertex = parents[current_vertex]
                route.appendleft(current_vertex)
                if current_vertex == start_vertex:
                    path.route = tuple(route)
                    path.path_length = len(route) - 1
                    return path

            path.route = None
            path.path_length = math.inf
            return path

        def __repr__(self):
            return ' -> '.join([str(path_node) for path_node in self.route]) if self.route is not None else 'None'

    def __init__(self, graph: Graph, start_vertex: GraphNode, target_vertex: GraphNode):
        self.graph = graph
        self.visited: Dict[GraphNode, bool] = {}
        self.queue: List[GraphNode] = []
        self.level: Dict[GraphNode, int] = {}
        self.parent: Dict[GraphNode: int] = {}
        self.bfs(start_vertex, target_vertex)
        self.path = self.Path.calculate_path(self.parent, start_vertex, target_vertex)

    def bfs(self, start_vertex: GraphNode, target_vertex: GraphNode) -> None:
        self.bfs_visit(start_vertex, target_vertex)

    def bfs_visit(self, start_vertex: GraphNode, target_vertex: GraphNode) -> None:
        self.visited[start_vertex] = True
        self.queue.append(start_vertex)
        current_level = 0
        while self.queue:
            current_vertex = self.queue.pop(0)
            for neighbor in self.graph.adjacency_list[current_vertex]:
                if neighbor.value == target_vertex.value:
                    self.visited[neighbor] = True
                    self.parent[neighbor] = current_vertex
                    self.level[neighbor] = current_level
                    return
                if not neighbor in self.visited or not self.visited[neighbor]:
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

    def bfs(self) -> None:
        for start_vertex in self.graph.vertices:
            if start_vertex not in self.visited:
                self.bfs_visit(start_vertex)

    def bfs_visit(self, start_vertex: GraphNode) -> None:
        self.visited[start_vertex] = True
        self.queue.append(start_vertex)
        current_level = 0
        while self.queue:
            current_vertex = self.queue.pop(0)
            for neighbor in self.graph.adjacency_list[current_vertex]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    self.level[neighbor] = current_level
                    self.parent[neighbor] = current_vertex
                    self.queue.append(neighbor)
            current_level += 1
