from OrderVector import OrderVector
from Route import Route
from Vertex import Vertex
import Adjacent


class AStar:
    def __init__(self, goal):
        self.goal = goal
        self.found_goal = False
        self.result = []
        self.path_cost = 0

    def search(self, current_vertex, value=0):
        # print('------------------')
        # print('current: {}'.format(current_vertex.label))
        self.result.append(current_vertex)
        self.path_cost += value
        current_vertex.visited = True

        if current_vertex == self.goal:
            self.found_goal = True
        else:
            order_vector = OrderVector(capacity=len(current_vertex.adjacents))
            for adjacent in current_vertex.adjacents:
                if not adjacent.vertex.visited:
                    adjacent.vertex.visited = True
                    order_vector.insert_in_vector(adjacent)
                    # order_vector.print_vector()

            if order_vector.values[0] is not None:
                self.search(order_vector.values[0].vertex, order_vector.values[0].cost)
        # return shortest path
        if not self.found_goal:
            return None, None
        return self.result, self.path_cost


def reset_visited_verticies(list_vertex):
    for vertex in list_vertex:
        vertex.visited = False