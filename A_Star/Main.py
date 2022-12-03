from Graph import Graph
from City import City
from Route import Route
from Vertex import Vertex
# from Data import data_cities
from Data2 import data_cities
import AStar
import logging


def process_data():
    cities_with_hospital = []
    cities_without_hospital_access = []
    graph = Graph()
    # Insert vertex in graph
    for element in data_cities:
        logging.info(f'Data.cities[{element}]={data_cities[element]}')
        has_hospital = False
        if data_cities[element]['hospital'] == 1:
            has_hospital = True
        city = City(label=element, has_hospital=has_hospital)
        vertex = Vertex(label=element, target_distance=0, vertex_object=city)
        if has_hospital:
            cities_with_hospital.append(vertex)
        else:
            cities_without_hospital_access.append(vertex)
        graph.add_vertex(vertex)
        logging.info('Inserting Vertex')

    for element in data_cities:
        # localizar as cidades do grafo pelo nome
        from_vertex = graph.search_vertex(element)
        if from_vertex is not None:
            logging.info(f'Data.cities[{element}]={data_cities[element]}')
            list_of_routes = data_cities[element]['routes']  # [{"Chernigov" : 56}, {"Lviv" : 107}]
            logging.info(f'list_of_routes={list_of_routes}')
            i = 0
            for route in list_of_routes:
                for k, v in route.items():
                    to_vertex = graph.search_vertex(k)
                    active = False
                    if data_cities[element]['active'][i] == 1:
                        active = True
                    # print(f'from_vertex={from_vertex.label} \tto_vertex={to_vertex.label}  \t active={active}')
                    route = Route(from_city=element, to_city=to_vertex.label, cost=v, active=active)
                    graph.create_adjacent(from_vertex=from_vertex, to_vertex=to_vertex, cost=v, adjacent_object=route)
                    logging.info('Inserting Adjacent')
                    i += 1

    return graph, cities_with_hospital, cities_without_hospital_access


def check_routes_to_rebuild(path, dist):
    # da cidade 1 para cidade 2
    # cidade 2 para cidade 3
    rebuild = {}
    # for city in path:
    for i in range(0, len(path), 2):
        city = path[i]
        if i + 1 >= len(city.adjacents):
            break
        index = 0
        while path[i+1] != city.adjacents[index].vertex:
            index += 1
            if index >= len(city.adjacents):
                break

        if not city.adjacents[index].adjacent_object.active:
            # print(f'city.adjacents[index].adjacent_object.active={city.adjacents[index].adjacent_object.active}')
            rebuild[city.adjacents[index].vertex] = {'path': path, 'dist': dist}
    return rebuild


def get_shortest_route(from_city, cities_with_hospital):
    min_dist = -1
    min_path_list = None
    for to_city in cities_with_hospital:
        a_star_search = AStar.AStar(to_city)
        AStar.reset_visited_verticies(cities_with_hospital)
        path_list, path_cost = a_star_search.search(from_city)

        if path_list is not None:
            if min_dist == -1:  # First time checking
                min_dist = path_cost
                min_path_list = path_list
            elif path_cost < min_dist:
                min_dist = path_cost
                min_path_list = path_list
        else:
            logging.info(f'path_list is None and to_city={to_city.label}')
    return min_path_list, min_dist


def main(cities_without_hospital_access, cities_with_hospital):
    rebuild = []
    for from_city in cities_without_hospital_access:
        # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$ NEW CITY $$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        # print(f"from_city={from_city.label}")
        path, dist = get_shortest_route(from_city, cities_with_hospital)
        if path is not None:
            for vertex in path:
                logging.info(f"vertex={vertex.label}\t")
            logging.info(f"dist={dist}")
            rebuild.append(check_routes_to_rebuild(path, dist))
        else:
            logging.info(f"Não achou caminho")
    return rebuild


def print_result(rebuild):
    print(f"------------ Rotas que precisam ser reconstruídas: ------------")
    new_list = []
    for r in rebuild:
        for vertex in r:
            string = ''
            for p in r[vertex]['path']:
                string += f'{p.label}\t'
                # print(f"{p.label}\t", end='')
            string += f'dist={r[vertex]["dist"]}'
            if string not in new_list:
                new_list.append(string)
                print(string)
            # print(f"dist={r[vertex]['dist']}")

graph, cities_with_hospital, cities_without_hospital_access = process_data()

# logging.error(f'cities_with_hospital')
# for city in cities_with_hospital:
#     logging.error(f'city={city.label}')
# logging.error(f'cities_without_hospital_access')
# for city in cities_without_hospital_access:
#     logging.error(f'city={city.label}')

# cities_without_hospital_access, cities_with_hospital = create_lists_based_on_hospital_access()
rebuild = main(cities_without_hospital_access, cities_with_hospital)
print_result(rebuild)
