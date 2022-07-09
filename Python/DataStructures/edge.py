from DataStructures.node import GraphNode


class GraphEdge:
    def __init__(self, node_a: GraphNode, node_b: GraphNode):
        self.node_a = node_a
        self.node_b = node_b

class UndirectedGraphEdge(GraphEdge):
    pass

class DirectedGraphEdge(GraphEdge):
    def __init__(self, start: GraphNode, end: GraphNode):
        self.start = start
        self.end = end

class UndirectedGraphEdgeWeighted(UndirectedGraphEdge):
    def __init__(self, node_a: GraphNode, node_b: GraphNode, weight: int):
        self.node_a = node_a
        self.node_b = node_b
        self.weight = weight

class DirectedGraphEdgeWeighted(DirectedGraphEdge):
    def __init__(self, start: GraphNode, end: GraphNode, weight: int):
        self.start = start
        self.end = end
        self.weight = weight