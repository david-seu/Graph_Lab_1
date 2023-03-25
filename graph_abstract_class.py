class DirectedGraph:

    def __init__(self, d_in=None, d_out=None, d_cost=None):
        if d_in is None:
            self.d_in = {}
        else:
            self.d_in = d_in
        if d_out is None:
            self.d_out = {}

        else:
            self.d_out = d_out
        if d_cost is None:
            self.d_cost = {}

        else:
            self.d_cost = d_cost

    def get_number_of_vertices(self):
        return len(self.d_in)

    def get_number_of_edges(self):
        return len(self.d_cost)

    def get_set_of_vertices(self):
        return list(self.d_in.keys())

    def get_set_of_edges(self):
        return self.d_cost.keys()

    def is_vertex(self, vertex):
        if vertex in self.d_in.keys():
            return True
        return False

    def is_edge(self, edge_vertices):
        if edge_vertices in list(self.d_cost.keys()):
            return True
        return False

    def add_vertex(self, vertex):
        if self.is_vertex(vertex):
            raise ValueError("Vertex already exists")
        self.d_in[vertex] = []
        self.d_out[vertex] = []

    def add_edge(self, edge_vertices, edge_cost):
        if self.is_edge(edge_vertices):
            raise ValueError("Edge already exists")
        if not (self.is_vertex(edge_vertices[0]) and self.is_vertex(edge_vertices[1])):
            raise ValueError("One or both vertices doesn't exist")
        self.d_in[edge_vertices[1]].append(edge_vertices[0])
        self.d_out[edge_vertices[0]].append(edge_vertices[1])
        self.d_cost[edge_vertices] = edge_cost

    def remove_vertex(self, vertex):
        if not self.is_vertex(vertex):
            raise ValueError("Vertex doesn't exist")
        for target_vertex in self.d_out[vertex]:
            self.d_in[target_vertex].remove(vertex)
            self.d_cost.pop((vertex, target_vertex))
        self.d_out.pop(vertex)
        for origin_vertex in self.d_in[vertex]:
            self.d_out[origin_vertex].remove(vertex)
            self.d_cost.pop((origin_vertex, vertex))
        self.d_in.pop(vertex)

    def remove_edge(self, edge_vertices):
        if not self.is_edge(edge_vertices):
            raise ValueError("Edge doesn't exist")
        self.d_cost.pop(edge_vertices)
        self.d_out[edge_vertices[0]].remove(edge_vertices[1])
        self.d_in[edge_vertices[1]].remove(edge_vertices[0])

    def get_in_degree(self, vertex):
        return len(self.d_in[vertex])

    def get_out_degree(self, vertex):
        return len(self.d_out[vertex])

    def set_cost_edge(self, edge_vertices, new_cost_edge):
        if not self.is_edge(edge_vertices):
            raise ValueError("Edge doesn't exist")
        self.d_cost[edge_vertices] = new_cost_edge

    def get_cost_edge(self, edge_vertices):
        if not self.is_edge(edge_vertices):
            raise ValueError("Edge doesn't exist")
        return self.d_cost[edge_vertices]

    def get_outbound_edges(self, vertex):
        if not self.is_vertex(vertex):
            raise ValueError("Vertex doesn't exist")
        return self.d_out[vertex]

    def get_inbound_edges(self, vertex):
        if not self.is_vertex(vertex):
            raise ValueError("Vertex doesn't exist")
        return self.d_in[vertex]

    def copy_graph(self):
        copy_graph = DirectedGraph()
        for vertex in list(self.d_in.keys()):
            copy_graph.d_in[vertex] = self.get_inbound_edges(vertex)
            copy_graph.d_out[vertex] = self.get_outbound_edges(vertex)
        for edge in list(self.d_cost.keys()):
            copy_graph.d_cost[edge] = self.d_cost[edge]
        return copy_graph
