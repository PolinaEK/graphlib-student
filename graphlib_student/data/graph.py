class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def add_edge(self, u, v, weight=1):
        self.edges.setdefault(u, []).append(v)
        self.weights[(u, v)] = weight

    def neighbors(self, node):
        return self.edges.get(node, [])

    def get_weight(self, u, v):
        return self.weights.get((u, v), None)