import networkx as nx
import matplotlib.pyplot as plt


###Завдання 1

G = nx.Graph()

stations = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F']

routes = [('Station A', 'Station B', 6),
          ('Station B', 'Station C', 2),
          ('Station C', 'Station D', 8),
          ('Station D', 'Station E', 2),
          ('Station E', 'Station F', 9),
          ('Station A', 'Station C', 3),
          ('Station B', 'Station D', 7),
          ('Station C', 'Station E', 3)]

G.add_nodes_from(stations)
G.add_weighted_edges_from(routes)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color='blue', font_size=8, font_weight='bold', node_size=2000)
nx.draw_networkx_edges(G, pos, edgelist=routes, edge_color='gray')

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Транспортна мережа міста")
plt.show()

num_of_nodes = G.number_of_nodes()
num_of_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин (станцій): {num_of_nodes}")
print(f"Кількість ребр (маршрутів): {num_of_edges}")
print("Ступені вершин (кількість з'єднань кожної станції):")
for station, degree in degrees.items():
    print(f"{station}: {degree}")


####Завдання 2
start_station = 'Station A'

  #Обхід у глибину
def dfs_recursive(graph:nx.Graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)

    for neighbor in graph.neighbors(vertex):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited

visited_stations_dfs = dfs_recursive(G, start_station)

print("\nDFS обхід у глибину з 'Station A': ")
for station_visited_dfs in visited_stations_dfs:
    print(f"\n {station_visited_dfs}")


  #Обхід у ширину
from collections import deque

def bfs_iterative(graph:nx.Graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph.neighbors(vertex)) - visited)

    return visited

visited_stations_bfs = bfs_iterative(G, start_station)

print("\nBFS обхід у ширину з 'Station A': ")
for station_visited_bfs in visited_stations_bfs:
    print(f"\n {station_visited_bfs}")
