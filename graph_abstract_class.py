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




