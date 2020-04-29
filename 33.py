import random
from math import sqrt
import triangle as triangle
import matplotlib.pyplot as plt

list_of_vertices = []

for i in range(100):
    x = random.randint(-20, 20)
    y = random.randint(-20, 20)
    list_of_vertices.append([x, y])
s = []
for i in range(100):
    for j in range(100):
        s.append([i, j])
A = dict(vertices=list_of_vertices, segments=s)
t = triangle.triangulate(A, 'e')
edges = t['edges'].tolist()
for i, item in enumerate(edges):
    item.append(sqrt((list_of_vertices[item[0]][0]
                      - list_of_vertices[item[1]][0]) ** 2
                     + (list_of_vertices[item[0]][1]
                        - list_of_vertices[item[1]][1]) ** 2))
triangle.compare(plt, A, t)
plt.show()

f = open('file.wug', 'w')
for i, item in enumerate(edges):
    f.write(str(item[0]) + ' ' + str(item[1]) + ' ' + str(item[2]) + ' \n')
f.close()

greatest_node = -1.0
graph = []
file = open('file.wug', "r")
for line in file:

    if not ("//" in line):
        info = line.split(" ")
        arrest = {info[0] + " & " + info[1]: info[2].replace('\n', '')}
        greatest_node = max(greatest_node, float(info[0]), float(info[1]))
        graph.append(arrest)
nodes = greatest_node + 1.0
prim = []

min_dist = {}
added = []

added.append(float(list(graph[0].keys())[0].split("&")[0]))
i = 0
while i < nodes:
    for node in range(len(graph)):
        n = list(graph[node].keys())[0].split("&")

        if (float(n[0]) in added or float(n[1]) in added) and (float(n[0]) not in added or float(n[1]) not in added):
            
            if len(min_dist) == 0:
                min_dist = graph[node]
            elif float(list(graph[node].values())[0]) < float(list(min_dist.values())[0]):
                min_dist = graph[node]
    if min_dist:
        prim.append(min_dist)
        if float(list(min_dist.keys())[0].split("&")[0]) not in added:
            added.append(float(list(min_dist.keys())[0].split("&")[0]))

        if float(list(min_dist.keys())[0].split("&")[1]) not in added:
            added.append(float(list(min_dist.keys())[0].split("&")[1]))
    min_dist = {}
    i += 1

print("\n\nMST nodes\n\n")
print(prim)
print("\n\nFinal cost:")
cost = 0
for i in prim:
    if i:
        cost += float(list(i.values())[0])
print(cost)
