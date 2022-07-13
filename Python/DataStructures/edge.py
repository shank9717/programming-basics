from DataStructures.node import GraphNode


class GraphEdge:
    def __init__(self, node_a: GraphNode, node_b: GraphNode):
        self.node_a = node_a
        self.node_b = node_b
        self.directed = False
        self.weight = 1


class UndirectedGraphEdge(GraphEdge):
    def __init__(self, node_a: GraphNode, node_b: GraphNode):
        super().__init__(node_a, node_b)
        self.directed = False


class DirectedGraphEdge(GraphEdge):
    def __init__(self, node_a: GraphNode, node_b: GraphNode):
        super().__init__(node_a, node_b)
        self.directed = True


class UndirectedGraphEdgeWeighted(UndirectedGraphEdge):
    def __init__(self, node_a: GraphNode, node_b: GraphNode, weight: int):
        super().__init__(node_a, node_b)
        self.weight = weight


class DirectedGraphEdgeWeighted(DirectedGraphEdge):
    def __init__(self, node_a: GraphNode, node_b: GraphNode, weight: int):
        super().__init__(node_a, node_b)
        self.weight = weight
