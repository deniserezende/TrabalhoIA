class Vertex:
  def __init__(self, label, target_distance, vertex_object):
    self.label = label
    self.adjacents = []
    self.target_distance = target_distance
    self.visited = False
    self.object = vertex_object  # City

  def add_adjacent_to_vertex(self, adjacent):
    self.adjacents.append(adjacent)

#   def print_vertex_and_adjacents(self):
#     for i in self.adjacents:
#         print(i.vertex.label, i.cost)

