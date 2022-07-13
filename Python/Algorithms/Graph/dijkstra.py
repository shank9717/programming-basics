from collections import deque
from typing import Dict, List, Optional, Tuple

from DataStructures.graphs import Graph
from DataStructures.node import GraphNode


class Dijkstra:
    class Path:
        def __init__(self, route: Tuple[GraphNode] = None, path_length: int = float('inf')):
            self.route = route
            self.path_length = path_length

        @staticmethod
        def calculate_path(distance: Dict[GraphNode, int], parents: Dict[GraphNode, GraphNode], start_vertex: GraphNode,
                           target_vertex: GraphNode):
            path = Dijkstra.Path()
            route = deque()
            path.path_length = distance[target_vertex]
            if target_vertex == start_vertex:
                path.route = (target_vertex,)
                return path

            current_vertex = target_vertex
            route.appendleft(current_vertex)
            while current_vertex in parents:
                current_vertex = parents[current_vertex]
                route.appendleft(current_vertex)
                if current_vertex == start_vertex:
                    path.route = tuple(route)
                    return path

            path.route = None
            path.path_length = float('inf')
            return path

        def __repr__(self):
            return ' -> '.join([str(path_node) for path_node in self.route]) if self.route is not None else 'None'

    # Below implementation of Dijkstra would be O(V^2)  - (or worse) due to poor choice of data structure.
    def __init__(self, graph: Graph, start_vertex: GraphNode):
        self.graph = graph
        self.start_vertex = start_vertex
        self.parent: Dict[GraphNode, Optional[GraphNode]] = {
            start_vertex: None
        }
        self.distance = {vertex: float('inf') for vertex in self.graph.vertices}
        self.distance[start_vertex] = 0

        self.processed_vertices = []
        self.vertices_to_be_processed = [vertex for vertex in graph.vertices]
        while len(self.vertices_to_be_processed) > 0:
            vertex = self.extract_min(self.vertices_to_be_processed)
            for neighbour in self.graph.adjacency_list[vertex]:
                distance_from_vertex = self.distance[vertex] + self.graph.get_edge(vertex, neighbour).weight
                if distance_from_vertex < self.distance[neighbour]:
                    self.parent[neighbour] = vertex
                    self.distance[neighbour] = distance_from_vertex

    def find_path(self, target_vertex: GraphNode):
        path = self.Path.calculate_path(self.distance, self.parent, self.start_vertex, target_vertex)
        return path

    def extract_min(self, vertices: List[GraphNode]):
        min_vertex = vertices[0]
        for vertex in vertices:
            if self.distance[vertex] < self.distance[min_vertex]:
                min_vertex = vertex
        self.vertices_to_be_processed.remove(min_vertex)
        self.processed_vertices.append(min_vertex)
        return min_vertex
