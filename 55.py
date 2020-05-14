 
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
   
class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph 
        self. ROW = len(graph) 
          
    def BFS(self,s, t, parent, G): 
  
        visited =[False]*(self.ROW) 
          
        queue=[] 
           
        queue.append(s) 
        visited[s] = True

        self.color_map = ['green' if node_visit else 'grey' for node_visit in visited]
        for i in parent:
            self.color_map[i] = 'green'
        self.color_map[t] = 'blue'
        plt.subplot()
        nx.draw_shell(G, node_color=self.color_map, node_size=900, with_labels=True, width=3)
        plt.show()
        
        while queue: 
  
            u = queue.pop(0) 

            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
        
        return True if visited[t] else False

    def FordFulkerson(self, source, sink, G): 

        parent = [-1]*(self.ROW) 
  
        max_flow = 0  

        while self.BFS(source, sink, parent, G) : 

            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 

            max_flow +=  path_flow 

            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
  
        return max_flow 
  
graph = [[0, 12, 10, 10, 10, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 7, 3, 1, 0, 0], 
        [0, 0, 0, 0, 0, 5, 4, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 4, 8, 0],
        [0, 0, 0, 0, 0, 0, 2, 4, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 15],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        ] 
  
g = Graph(graph)

G = nx.Graph()
G.add_edge(0, 1, weight=12)
G.add_edge(0, 2, weight=10)
G.add_edge(0, 3, weight=10)
G.add_edge(0, 4, weight=10)
G.add_edge(1, 5, weight=7)
G.add_edge(1, 6, weight=3)
G.add_edge(1, 7, weight=1)
G.add_edge(2, 5, weight=5)
G.add_edge(2, 6, weight=4)
G.add_edge(2, 7, weight=1)
G.add_edge(3, 6, weight=2)
G.add_edge(3, 7, weight=4)
G.add_edge(3, 8, weight=8)
G.add_edge(4, 6, weight=2)
G.add_edge(4, 7, weight=4)
G.add_edge(4, 8, weight=8)
G.add_edge(5, 9, weight=10)
G.add_edge(6, 9, weight=8)
G.add_edge(7, 9, weight=9)
G.add_edge(8, 9, weight=15)

  
source = 0; sink = 9
   
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink, G))
  
