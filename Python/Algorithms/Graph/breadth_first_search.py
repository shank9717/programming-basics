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
                if neighbor not in self.visited or not self.visited[neighbor]:
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


class BidirectionalBreadthFirstSearch:
    class Path:
        def __init__(self, route: Tuple[GraphNode] = None, path_length: int = math.inf):
            self.route = route
            self.path_length = path_length

        @staticmethod
        def form_path(source_parents: Dict[GraphNode, GraphNode], target_parents: Dict[GraphNode, GraphNode],
                      start_vertex: GraphNode, target_vertex: GraphNode, intersection_vertex: GraphNode):
            path = BreadthFirstSearch.Path()
            if intersection_vertex is None:
                return path

            route = deque()
            current_vertex = intersection_vertex
            route.appendleft(current_vertex)
            while current_vertex in source_parents:
                current_vertex = source_parents[current_vertex]
                route.appendleft(current_vertex)
                if current_vertex == start_vertex:
                    break

            current_vertex = intersection_vertex
            while current_vertex in target_parents:
                current_vertex = target_parents[current_vertex]
                route.append(current_vertex)
                if current_vertex == target_vertex:
                    break

            path.route = tuple(route)
            path.path_length = len(route) - 1
            return path

        def __repr__(self):
            return ' -> '.join([str(path_node) for path_node in self.route]) if self.route is not None else 'None'

    def __init__(self, graph: Graph, start_vertex: GraphNode, target_vertex: GraphNode):
        self.graph = graph
        self.source_visited: Dict[GraphNode, bool] = {}
        self.target_visited: Dict[GraphNode, bool] = {}

        self.source_queue: List[GraphNode] = []
        self.target_queue: List[GraphNode] = []

        self.source_parent: Dict[GraphNode: int] = {}
        self.target_parent: Dict[GraphNode: int] = {}

        intersection_vertex = self.bidirectional_bfs(start_vertex, target_vertex)
        self.path = self.Path.form_path(self.source_parent, self.target_parent,
                                        start_vertex, target_vertex, intersection_vertex)

    def bidirectional_bfs(self, start_vertex: GraphNode, target_vertex: GraphNode) -> GraphNode:
        return self.bidirectional_bfs_visit(start_vertex, target_vertex)

    def bidirectional_bfs_visit(self, start_vertex: GraphNode, target_vertex: GraphNode) -> GraphNode:
        self.source_visited[start_vertex] = True
        self.target_visited[target_vertex] = True

        self.source_queue.append(start_vertex)
        self.target_queue.append(target_vertex)

        while self.source_queue and self.target_queue:
            vertex_from_source = self.source_queue.pop(0)
            for neighbor in self.graph.adjacency_list[vertex_from_source]:
                if neighbor.value == target_vertex.value or neighbor in self.target_visited:
                    self.source_visited[neighbor] = True
                    self.source_parent[neighbor] = vertex_from_source
                    return neighbor
                if neighbor not in self.source_visited or not self.source_visited[neighbor]:
                    self.source_visited[neighbor] = True
                    self.source_parent[neighbor] = vertex_from_source
                    self.source_queue.append(neighbor)

            vertex_from_target = self.target_queue.pop(0)
            for neighbor in self.graph.adjacency_list[vertex_from_target]:
                if neighbor.value == start_vertex.value or neighbor in self.source_visited:
                    self.target_visited[neighbor] = True
                    self.target_parent[neighbor] = vertex_from_target
                    return neighbor
                if neighbor not in self.target_visited or not self.target_visited[neighbor]:
                    self.target_visited[neighbor] = True
                    self.target_parent[neighbor] = vertex_from_target
                    self.target_queue.append(neighbor)
