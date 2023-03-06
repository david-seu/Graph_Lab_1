COST = 2
VERTEX_IN = 1
VERTEX_OUT = 0
from graph_abstract_class import DirectedGraph

class Service:

    def __init__(self):
        self.graph = None

    def read_from_file_standard(self, file_name):
        d_in = {}
        d_out = {}
        d_cost = {}
        with open(file_name) as file:
            content = file.readlines()
            for vertex in range(int(content[0].split()[0])):
                d_in[vertex] = []
                d_out[vertex] = []
            for line in content[1:]:
                line = [int(value) for value in line.split()]
                d_out[line[VERTEX_OUT]].append(line[VERTEX_IN])
                d_in[line[VERTEX_IN]].append(line[VERTEX_OUT])
                d_cost[(line[VERTEX_OUT], line[VERTEX_IN])] = line[COST]
        self.graph = DirectedGraph(d_cost=d_cost, d_out=d_out, d_in=d_in)

    def get_number_of_vertices(self):
        return self.graph.get_number_of_vertices()


    def write_to_file_standard(self):
        pass





