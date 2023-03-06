class Console:

    def __init__(self, service):
        self.__service = service

    @staticmethod
    def __menu():
        return("""
    Commands:
    1. get the number of vertices
    2. get set of vertices
    3. add vertex
    4. add edge
    5. remove vertex
    6. remove edge
    7. check if edge exists
    8. get in degree of a vertex
    9. get out degree of a vertex
    10. get outbound edges of a vertex
    11. get inbound edges of a vertex
    12. get cost of an edge
    13. modify cost of an edge
    14. copy graph
    15. read from text file
    16. write to text file
    17. create random graph
        """)
    def run(self):
        commands = {
            1: self.__print_number_of_vertices,
            2: self.__print_set_vertices,
            3: self.__add_vertex,
            4: self.__add_edge,
            5: self.__remove_vertex,
            6: self.__remove_edge,
            7: self.__is_edge,
            8: self.__print_in_degree,
            9: self.__print_out_degree,
            10: self.__print_outbound_edges,
            11: self.__print_inbound_edges,
            12: self.__print_cost_edge,
            13: self.__modify_cost_edge,
            14: self.__copy_graph,
            15: self.__read_file,
            16: self.__write_file,
            17: self.__generate_random_graph

        }
        print(self.__menu())
        while True:
            while True:
                try:
                    command = int(input("Enter a command number: "))
                    if command not in range(1,18):
                        raise ValueError
                    break
                except ValueError:
                    print('Invalid command')
            try:
                commands[command]()
            except Exception:
                pass
            choice = bool(input("Want to see the menu again(T or F): "))
            if choice:
                print(self.__menu())

    def __print_number_of_vertices(self):
        print(f"Number of vertices: {self.__service.get_number_of_vertices()}")

    def __print_set_vertices(self):
        pass

    def __add_vertex(self):
        pass

    def __add_edge(self):
        pass

    def __remove_vertex(self):
        pass

    def __remove_edge(self):
        pass

    def __is_edge(self):
        pass

    def __print_in_degree(self):
        pass

    def __print_out_degree(self):
        pass

    def __print_outbound_edges(self):
        pass

    def __print_inbound_edges(self):
        pass

    def __print_cost_edge(self):
        pass

    def __modify_cost_edge(self):
        pass

    def __copy_graph(self):
        pass

    def __read_file(self):
        file_name = input("Enter the file name: ")
        self.__service.read_from_file_standard(file_name)

    def __write_file(self):
        pass

    def __generate_random_graph(self):
        pass





