class Service:

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
                vertex
