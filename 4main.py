import heapq
import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
	def __init__(self, nodes):
		self.nodes = set(nodes)
		self.edges = {}
		for node in nodes:
			self.edges[node] = {}

	def connect(self, x, y, value):
		self.edges[x][y] = value
		self.edges[y][x] = value

	def dikjstra(self, start):
		dist = {}
		path = {}
		unvisited = []
		for node in self.nodes:
			if node == start:
				dist[start] = 0
			else:
				dist[node] = sys.maxsize
			path[node] = []
			heapq.heappush(unvisited, (dist[node], node))

		while unvisited:
			weight, u = heapq.heappop(unvisited)
			for neighbor in self.edges[u]:
				temp_dist = dist[u] + self.edges[u][neighbor]
				if temp_dist < dist[neighbor]:
					remove_and_update_priority(unvisited, dist, neighbor, temp_dist)
					dist[neighbor] = temp_dist
					path[neighbor] = path[u] + [u]
		return dist, path
		
def remove_and_update_priority(heap, dist, node, value):
	for index, item in enumerate(heap):
		distance,potential_node = item[0], item[1]
		if potential_node == node and distance == dist[node]:
			heap.pop(index)
	heapq.heappush(heap, (value, node))


nodes = [1,2,3,4,5,6]
graph = Graph(nodes)
G=nx.DiGraph()
#graph.connect(cоединяемые вершины + вес)
graph.connect(1,2,3)
G.add_edge(1,2,weight=3)
graph.connect(1,3,1)
G.add_edge(1,3,weight=1)
graph.connect(2,4,4)
G.add_edge(2,4,weight=4)
graph.connect(2,5,1)
G.add_edge(2,5,weight=1)
graph.connect(3,5,5)
G.add_edge(3,5,weight=5)
graph.connect(5,6,9)
G.add_edge(5,6,weight=9)
graph.connect(4,6,2)
G.add_edge(4,6,weight=2)
#graph.dikjstra(стартовая вершина)
print(graph.dikjstra(2))

pos = nx.shell_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='red')
nx.draw_networkx_edges(G, pos, width=3, alpha=0.8)
nx.draw_networkx_labels(G, pos, font_size=20)
plt.show()

