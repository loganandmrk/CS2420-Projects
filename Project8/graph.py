import math

class Graph:
    class Vertex:
        def __init__(self, label):
            self.label = label

    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
    
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
    
    def _vertex_by_label(self, label):
        for vertex in self.adjacency_list.keys():
            if getattr(vertex, "label", None) == label:
                return vertex
        raise KeyError(f"No vertex with label {label!r}")

    def add_edge(self, from_vertex, to_vertex, weight=1):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def get_weight(self, from_vertex, to_vertex):
        if (from_vertex, to_vertex) not in self.edge_weights:
            return math.inf
        elif to_vertex not in self.adjacency_list[from_vertex]:
            raise ValueError("No edge exists between the specified vertices.")

        return self.edge_weights.get((from_vertex, to_vertex), None)

    def dfs(self, start_vertex):
        from collections import deque
        #return a generator for traversing the graph in depth first order starting from start_vertex
        start_vertex = self._vertex_by_label(start_vertex)
        discovered_set = {start_vertex}
        frontier = deque([start_vertex])
        visited_list = []
        distances = {start_vertex: 0}
        while frontier:  # stops when empty
            current_vertex = frontier.popleft()
            visited_list.append(current_vertex)
            for adjacent in self.adjacency_list[current_vertex]:
                if adjacent not in discovered_set:
                    discovered_set.add(adjacent)
                    frontier.append(adjacent)
                    distances[adjacent] = distances[current_vertex] + 1
        return visited_list

    def bfs(self, start_vertex):
        #return a generator for traversing the graph in breadth first order starting from start_vertex
        discovered_set = set()
        frontier_queue = []
        visited_list = []

        distances = {}
        distances[start_vertex] = 0

        frontier_queue.append(start_vertex)
        discovered_set.add(start_vertex)

        while frontier_queue is not None:
            current_vertex = frontier_queue.pop(0)
            visited_list.append(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in discovered_set:
                    frontier_queue.append(adjacent_vertex)
                    discovered_set.add(adjacent_vertex)
                    distances[adjacent_vertex] = distances[current_vertex] + 1
        return visited_list

    def dsp(self, dest_vertex):
        #return a tuple (path length, path list). If no path exists return the tuple (math.inf, [])
        pass



    #def dsp_all(self):
        #pass

    def __str__(self):
        result = "digraph G {\n"
        for vertex in self.adjacency_list:
            for edge in self.adjacency_list[vertex]:
                weight = self.get_weight(vertex, edge)
                result += f'  {vertex.label} -> {edge.label} [label="{float(weight)}",weight="{float(weight)}"];\n'
        result += "}"

        return result