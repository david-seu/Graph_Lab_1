import random
from random import randint

COST = 2
VERTEX_IN = 1
VERTEX_OUT = 0
from graph_abstract_class import DirectedGraph


class Service:

    def __init__(self):
        self.graph = None
        self.graph_copy = None

    def read_from_file_standard(self, file_name):
        self.graph = DirectedGraph()
        with open(file_name) as file:
            content = file.readlines()
            for vertex in range(int(content[0].split()[0])):
                self.add_vertex(vertex)
            for line in content[1:]:
                line = [int(value) for value in line.split()]
                self.graph.add_edge((line[VERTEX_OUT], line[VERTEX_IN]), line[COST])

    def read_from_file(self, file_name):
        self.graph = DirectedGraph()
        with open(file_name) as file:
            content = file.readlines()
            for line in content:
                line = [int(value) for value in line.split()]
                if line[VERTEX_IN] == -1:
                    self.graph.add_vertex(line[VERTEX_OUT])
                else:
                    try:
                        self.graph.add_vertex(line[VERTEX_IN])
                    except ValueError:
                        pass
                    try:
                        self.graph.add_vertex(line[VERTEX_OUT])
                    except ValueError:
                        pass
                    self.graph.add_edge((line[VERTEX_OUT], line[VERTEX_IN]), line[COST])

    def write_to_file_standard(self, file_name):
        if self.graph is None:
            raise ValueError("No graph in memory")
        with open(file_name, 'w') as file:
            file.write(f'{self.get_number_of_vertices()}' + ' ' + f'{self.get_number_of_edges()}' + '\n')
            edges = self.graph.get_set_of_edges()
            for edge in edges:
                file.write(f'{edge[0]}' + ' ' + f'{edge[1]}' + ' ' + f'{self.get_cost_edge(edge)}' + '\n')

    def write_to_file(self, file_name):
        if self.graph is None:
            raise ValueError("No graph in memory")
        with open(file_name, 'w') as file:
            edges = self.graph.get_set_of_edges()
            for edge in edges:
                file.write(f'{edge[0]}' + ' ' + f'{edge[1]}' + ' ' + f'{self.get_cost_edge(edge)}' + '\n')
            for vertex in self.graph.d_in.keys():
                if len(self.graph.d_in[vertex]) == 0 and len(self.graph.d_out[vertex] == 0):
                    file.write(f'{vertex}' + ' ' + '-1' + ' ' + '\n')

    def get_number_of_edges(self):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_number_of_edges()

    def get_number_of_vertices(self):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_number_of_vertices()

    def get_set_of_edges(self):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_set_of_edges()

    def get_set_of_vertices(self):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_set_of_vertices()

    def add_vertex(self, vertex):
        if self.graph is None:
            raise ValueError("No graph in memory")
        self.graph.add_vertex(vertex)

    def add_edge(self, edge_vertices, edge_cost):
        if self.graph is None:
            raise ValueError("No graph in memory")
        self.graph.add_edge(edge_vertices, edge_cost)

    def is_edge(self, edge_vertices):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.is_edge(edge_vertices)

    def get_in_degree(self, vertex):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_in_degree(vertex)

    def get_out_degree(self, vertex):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_out_degree(vertex)

    def get_cost_edge(self, edge_vertices):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_cost_edge(edge_vertices)

    def set_cost_edge(self, edge_vertices, new_cost_edge):
        if self.graph is None:
            raise ValueError("No graph in memory")
        self.graph.set_cost_edge(edge_vertices, new_cost_edge)

    def get_outbound_edges(self, vertex):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_outbound_edges(vertex)

    def get_inbound_edges(self, vertex):
        if self.graph is None:
            raise ValueError("No graph in memory")
        return self.graph.get_inbound_edges(vertex)

    def generate_random_graph(self, number_of_vertices, number_of_edges):
        if number_of_edges > number_of_vertices ** 2:
            raise ValueError("Invalid number of edges")
        random_graph = DirectedGraph()
        for vertex in range(number_of_vertices):
            random_graph.add_vertex(vertex)
        for edge in range(number_of_edges):
            while True:
                vertex_in = random.choice(list(random_graph.d_in.keys()))
                vertex_out = random.choice(list(random_graph.d_in.keys()))
                edge_cost = randint(1, 50)
                try:
                    random_graph.add_edge((vertex_in, vertex_out), edge_cost)
                except Exception:
                    pass
                else:
                    break
        self.graph = random_graph

    def remove_vertex(self, vertex):
        if self.graph is None:
            raise ValueError("No graph in memory")
        self.graph.remove_vertex(vertex)

    def remove_edge(self, edge_vertices):
        if self.graph is None:
            raise ValueError("No graph in memory")
        self.graph.remove_edge(edge_vertices)

    def copy_graph(self):
        if self.graph is None:
            raise ValueError("No graph in memory")
        self.graph_copy = self.graph.copy_graph()

    def make_copy_graph_main_graph(self):
        if self.graph_copy is None:
            raise ValueError("No graph copy in memory")
        self.graph, self.graph_copy = self.graph_copy, self.graph

    def get_lowest_length_path(self, vertex1, vertex2):
        accessible, length = self.graph.get_all_accessible_vertices(vertex1)
        try:
            return length[vertex2]
        except KeyError:
            raise ValueError("Vertex is not accessible")

