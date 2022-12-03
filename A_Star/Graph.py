from Vertex import Vertex
from Adjacent import Adjacent

class Graph:
    def __init__(self):
        self.vertices = []

    def create_vertex(self, label, target_distance, vertex_object):
        vertex = Vertex(label, target_distance, vertex_object)
        self.vertices.append(vertex)

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def create_adjacent(self, from_vertex, to_vertex, cost, adjacent_object):
        adjacent = Adjacent(to_vertex, cost, adjacent_object)
        from_vertex.add_adjacent_to_vertex(adjacent)

    def search_vertex(self, label):
        for vertex in self.vertices:
            if vertex.label == label:
                return vertex
        return None

