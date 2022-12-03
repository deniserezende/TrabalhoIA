import numpy as np


class OrderVector:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lastFilledPosition = -1
        # Mudança no tipo de dados
        self.values = np.empty(self.capacity, dtype=object)

    # Referência para o vértice e comparação com a distância para o objetivo
    def insert_in_vector(self, adjacent):
        if self.lastFilledPosition == self.capacity - 1:
            print('Capacidade máxima atingida')
            return
        position = 0
        for i in range(self.lastFilledPosition + 1):
            position = i
            if self.values[i].distancia_aestrela > adjacent.distancia_aestrela:
                break
            if i == self.lastFilledPosition:
                position = i + 1
        x = self.lastFilledPosition
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1
        self.values[position] = adjacent
        self.lastFilledPosition += 1

    def print_vector(self):
        if self.lastFilledPosition == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.lastFilledPosition + 1):
                print(i, ' - ', self.values[i].vertex.label, ' - ',
                      self.values[i].cost, ' - ',
                      self.values[i].vertex.target_distance, ' - ',
                      self.values[i].distancia_aestrela)
