
class Adjacent:
  def __init__(self, vertex, cost, adjacent_object):
    self.vertex = vertex
    self.cost = cost
    self.adjacent_object = adjacent_object # ROTA - custo e se está ativo ou não

    # # Novo atributo
    # # TODO não entendi
    self.distancia_aestrela = vertex.target_distance + self.cost
