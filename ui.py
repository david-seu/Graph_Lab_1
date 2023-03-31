class Console:

    def __init__(self, service):
        self.__service = service

    @staticmethod
    def __menu():
        return ("""
    Commands:
    1. get the number of vertices
    2. get set of vertices
    3. get the number of edges
    4. get set of edges
    5. add vertex
    6. add edge
    7. remove vertex
    8. remove edge
    9. check if edge exists
    10. get in degree of a vertex
    11. get out degree of a vertex
    12. get outbound edges of a vertex
    13. get inbound edges of a vertex
    14. get cost of an edge
    15. modify cost of an edge
    16. copy graph
    17. read from text file
    18. write to text file
    19. read from text file standard
    20. write to text file standard
    21. create random graph
    22. Make copy graph main graph
    23. Get lowest length path between 2 vertices
        """)

    def run(self):
        commands = {
            1: self.__print_number_of_vertices,
            2: self.__get_set_vertices,
            3: self.__print_number_of_edges,
            4: self.__get_set_of_edges,
            5: self.__add_vertex,
            6: self.__add_edge,
            7: self.__remove_vertex,
            8: self.__remove_edge,
            9: self.__is_edge,
            10: self.__print_in_degree,
            11: self.__print_out_degree,
            12: self.__print_outbound_edges,
            13: self.__print_inbound_edges,
            14: self.__print_cost_edge,
            15: self.__modify_cost_edge,
            16: self.__copy_graph,
            17: self.__read_file,
            18: self.__write_file,
            19: self.__read_file_standard,
            20: self.__write_file_standard,
            21: self.__generate_random_graph,
            22: self.__make_copy_main_graph,
            23: self.__get_lowest_length_path

        }
        print(self.__menu())
        while True:
            while True:
                try:
                    command = int(input("Enter a command number: "))
                    if command not in range(1, 24):
                        raise ValueError
                    break
                except ValueError:
                    print('Invalid command')
            try:
                commands[command]()
            except Exception as error:
                print(error)
            choice = input("Want to see the menu again(T or F): ").upper()
            if choice == "T":
                print(self.__menu())

    def __print_number_of_vertices(self):
        print(f"Number of vertices: {self.__service.get_number_of_vertices()}")

    def __get_set_vertices(self):
        print("The set of vertices is: ")
        print(sorted(self.__service.get_set_of_vertices()))

    def __print_number_of_edges(self):
        print(f"Number of edges: {self.__service.get_number_of_edges()}")

    def __get_set_of_edges(self):
        print("The set of edges is: ")
        print(list(self.__service.get_set_of_edges()))

    def __add_vertex(self):
        vertex = int(input("Enter the label of the vertex: "))
        self.__service.add_vertex(vertex)

    def __add_edge(self):
        edge = [int(vertex) for vertex in input("Enter the edge (vertex_in, vertex_out, cost): ").split()]
        edge_vertices = tuple(edge[:2])
        edge_cost = edge[-1]
        self.__service.add_edge(edge_vertices, edge_cost)

    def __remove_vertex(self):
        vertex = int(input("Enter the vertex: "))
        self.__service.remove_vertex(vertex)

    def __remove_edge(self):
        edge_vertices = tuple([int(vertex) for vertex in input("Enter the vertices of the edge: ").split()])
        self.__service.remove_edge(edge_vertices)

    def __is_edge(self):
        edge_vertices = tuple([int(vertex) for vertex in input("Enter the vertices of the edge: ").split()])
        if self.__service.is_edge(edge_vertices):
            print("Edge exists")
        else:
            print("Edge doesn't exist")

    def __print_in_degree(self):
        vertex = int(input("Enter the vertex: "))
        print(self.__service.get_in_degree(vertex))

    def __print_out_degree(self):
        vertex = int(input("Enter the vertex: "))
        print(self.__service.get_out_degree(vertex))

    def __print_outbound_edges(self):
        vertex = int(input("Enter the vertex: "))
        print("The set of target vertices is: ")
        print(self.__service.get_outbound_edges(vertex), sep=' ')

    def __print_inbound_edges(self):
        vertex = int(input("Enter the vertex: "))
        print("The set of origin vertices is: ")
        print(self.__service.get_inbound_edges(vertex), sep=' ')

    def __print_cost_edge(self):
        edge_vertices = tuple([int(vertex) for vertex in input("Enter the vertices of the edge: ").split()])
        print(self.__service.get_cost_edge(edge_vertices))

    def __modify_cost_edge(self):
        data = [int(integer) for integer in
                input("Enter the edge you want to modify(vertex_in, vertex_out, new_cost): ").split()]
        vertices = tuple(data[:2])
        new_cost_edge = data[-1]
        self.__service.set_cost_edge(vertices, new_cost_edge)

    def __copy_graph(self):
        self.__service.copy_graph()

    def __read_file_standard(self):
        file_name = input("Enter the file name: ")
        self.__service.read_from_file_standard(file_name)

    def __read_file(self):
        file_name = input("Enter the file name: ")
        self.__service.read_from_file(file_name)

    def __write_file(self):
        file_name = input("Enter the file name: ")
        self.__service.write_to_file(file_name)

    def __write_file_standard(self):
        file_name = input("Enter the file name: ")
        self.__service.write_to_file_standard(file_name)

    def __generate_random_graph(self):
        number_of_vertices, number_of_edges = input("Enter the number of vertices and edges: ").split()
        self.__service.generate_random_graph(int(number_of_vertices), int(number_of_edges))
        self.__get_set_vertices()
        self.__get_set_of_edges()

    def __make_copy_main_graph(self):
        self.__service.make_copy_graph_main_graph()

    def __get_lowest_length_path(self):
        vertex1, vertex2 = input("Enter the start and end vertices: ").split()
        print(self.__service.get_lowest_length_path(int(vertex1), int(vertex2)))
