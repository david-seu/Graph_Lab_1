import queue
import math


class DirectedGraph:

    def __init__(self, d_in=None, d_out=None, d_cost=None):
        """
          Constructor for the DirectedGraph class.

          Args:
          - d_in (dict): Dictionary representing incoming edges.
          - d_out (dict): Dictionary representing outgoing edges.
          - d_cost (dict): Dictionary representing edge costs.
        """
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
        """
        Returns the number of vertices in the graph.
        """
        return len(self.d_in)

    def get_number_of_edges(self):
        """
        Returns the number of edges in the graph.
        """
        return len(self.d_cost)

    def get_set_of_vertices(self):
        """
        Returns a list of all vertices in the graph.
        """
        return list(self.d_in.keys())

    def get_set_of_edges(self):
        """
        Returns a set of all edges in the graph.
        """
        return self.d_cost.keys()

    def is_vertex(self, vertex):
        """
        Returns True if the vertex is in the graph, otherwise returns False.

        Args:
        - vertex: The vertex to check.
        """
        if vertex in self.d_in.keys():
            return True
        return False

    def is_edge(self, edge_vertices):
        """
        Returns True if the edge is in the graph, otherwise returns False.

        Args:
        - edge_vertices: A tuple representing the edge.
        """
        if edge_vertices in list(self.d_cost.keys()):
            return True
        return False

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Args:
        - vertex: The vertex to add.
        """
        if self.is_vertex(vertex):
            raise ValueError("Vertex already exists")
        self.d_in[vertex] = []
        self.d_out[vertex] = []

    def add_edge(self, edge_vertices, edge_cost):
        """
        Adds an edge to the graph.

        Args:
        - edge_vertices: A tuple representing the edge.
        - edge_cost: The cost of the edge.
        """
        if self.is_edge(edge_vertices):
            raise ValueError("Edge already exists")
        if not (self.is_vertex(edge_vertices[0]) and self.is_vertex(edge_vertices[1])):
            raise ValueError("One or both vertices doesn't exist")
        self.d_in[edge_vertices[1]].append(edge_vertices[0])
        self.d_out[edge_vertices[0]].append(edge_vertices[1])
        self.d_cost[edge_vertices] = edge_cost

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph.

        Args:
        - vertex: The vertex to remove.
        """
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
        """
        Remove an edge from the graph.

        Args:
        - edge_vertices (tuple): A tuple containing the source and target vertices of the edge to be removed.

        Raises:
        - ValueError: If the edge does not exist in the graph.
        """
        if not self.is_edge(edge_vertices):
            raise ValueError("Edge doesn't exist")
        self.d_cost.pop(edge_vertices)
        self.d_out[edge_vertices[0]].remove(edge_vertices[1])
        self.d_in[edge_vertices[1]].remove(edge_vertices[0])

    def get_in_degree(self, vertex):
        """
        Get the in-degree of a given vertex.

        Args:
        - vertex (int): The vertex for which to calculate the in-degree.

        Returns:
        - int: The in-degree of the given vertex.
        """
        return len(self.d_in[vertex])

    def get_out_degree(self, vertex):
        """
        Get the out-degree of a given vertex.

        Args:
        - vertex (int): The vertex for which to calculate the out-degree.

        Returns:
        - int: The out-degree of the given vertex.
        """
        return len(self.d_out[vertex])

    def set_cost_edge(self, edge_vertices, new_cost_edge):
        """
        Set the cost of a given edge.

        Args:
        - edge_vertices (tuple): A tuple containing the source and target vertices of the edge for which to set the cost.
        - new_cost_edge (float): The new cost of the given edge.

        Raises:
        - ValueError: If the edge does not exist in the graph.
        """
        if not self.is_edge(edge_vertices):
            raise ValueError("Edge doesn't exist")
        self.d_cost[edge_vertices] = new_cost_edge

    def get_cost_edge(self, edge_vertices):
        """
        Get the cost of a given edge.

        Args:
        - edge_vertices (tuple): A tuple containing the source and target vertices of the edge for which to get the cost.

        Returns:
        - float: The cost of the given edge.

        Raises:
        - ValueError: If the edge does not exist in the graph.
        """
        if not self.is_edge(edge_vertices):
            raise ValueError("Edge doesn't exist")
        return self.d_cost[edge_vertices]

    def get_outbound_edges(self, vertex):
        """
        Get a list of all outbound edges of a given vertex.

        Args:
        - vertex (int): The vertex for which to get the outbound edges.

        Returns:
        - list: A list of tuples containing the source and target vertices of all outbound edges of the given vertex.

        Raises:
        - ValueError: If the vertex does not exist in the graph.
        """
        if not self.is_vertex(vertex):
            raise ValueError("Vertex doesn't exist")
        return self.d_out[vertex]

    def get_inbound_edges(self, vertex):
        """
        Get a list of all inbound edges of a given vertex.

        Args:
        - vertex (int): The vertex for which to get the inbound edges.

        Returns:
        - list: A list of tuples containing the source and target vertices of all inbound edges of the given vertex.

        Raises:
        - ValueError: If the vertex does not exist in the graph.
        """
        if not self.is_vertex(vertex):
            raise ValueError("Vertex doesn't exist")
        return self.d_in[vertex]

    def copy_graph(self):
        """
        Create a copy of the current graph.

        Returns:
        - DirectedGraph: A new instance of DirectedGraph with the same vertices and edges as the current graph.
        """
        copy_graph = DirectedGraph()
        for vertex in list(self.d_in.keys()):
            copy_graph.d_in[vertex] = self.get_inbound_edges(vertex)
            copy_graph.d_out[vertex] = self.get_outbound_edges(vertex)
        for edge in list(self.d_cost.keys()):
            copy_graph.d_cost[edge] = self.d_cost[edge]
        return copy_graph

    def get_all_accessible_vertices(self, vertex1, vertex2):
        """
        Given two vertices, returns a dictionary containing the accessible vertices
        from vertex1, along with the vertex that was used to access each one.
        Uses a breadth-first search algorithm to traverse the graph.
        If vertex2 is reached during the search, the traversal is stopped early.

        Parameters:
        - vertex1 (int): the starting vertex for the traversal
        - vertex2 (int): the target vertex that, if reached, stops the traversal early

        Returns:
        - prev (dict): a dictionary containing the accessible vertices from vertex1
          along with the vertex that was used to access each one
        """
        q = queue.Queue()
        prev = {}
        visited = set()
        q.put(vertex1)
        visited.add(vertex1)
        while not q.empty():
            x = q.get()
            for y in self.d_out[x]:
                if y not in visited:
                    q.put(y)
                    visited.add(y)
                    prev[y] = x
                    if y == vertex2:
                        break
        return prev

    def calculate_minimum_cost_walk(self, vertex1):
        """
        Given two vertices, calculates the minimum cost walk from vertex1 to vertex2.
        Uses the Bellman-Ford algorithm to find the shortest path.

        Parameters:
        - vertex1 (int): the starting vertex for the walk

        Returns:
        - prev (dict): a dictionary containing the vertices along the shortest path from
          vertex1 to vertex2, along with the vertex that was used to access each one
        - dist (dict): a dictionary containing the minimum distance to reach each vertex
          from vertex1
        """
        dist = {}
        prev = {}
        for vertex in self.d_in.keys():
            dist[vertex] = math.inf
        dist[vertex1] = 0
        changed = True
        for _ in range(self.get_number_of_vertices()-1):
            changed = False
            for (x, y) in self.d_cost.keys():
                if dist[y] > dist[x] + self.d_cost[(x, y)]:
                    dist[y] = dist[x] + self.d_cost[(x, y)]
                    prev[y] = x
                    changed = True
            if not changed:
                return prev, dist
        for _ in range(self.get_number_of_vertices()-1):
            for (x, y) in self.d_cost.keys():
                if dist[y] > dist[x] + self.d_cost[(x, y)]:
                     raise ValueError("Negative cost cycle")