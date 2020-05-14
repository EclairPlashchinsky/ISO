from itertools import product
from math import inf

def floyd(n, edges):
    distance = [[inf] * n for i in range(n)]
    next = [[0] * n for i in range(n)]
    for i in range(n):
        distance[i][i] = 0
    for u, v, w in edges:
        distance[u - 1][v - 1] = w
        next[u - 1][v - 1] = v - 1
    for k, i, j in product(range(n), repeat=3):
        sum_ik_kj = distance[i][k] + distance[k][j]
        if distance[i][j] > sum_ik_kj:
            distance[i][j] = sum_ik_kj
            next[i][j] = next[i][k]
    for i, j in product(range(n), repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(next[path[-1]][j])
            print("От", (i+1), " до ", (j+1), ": ", ', '.join(str(p + 1) for p in path))
            print("Вес :", distance[i][j])

v = 3
edges = [[1, 2, 3], [1, 3, 1], [3, 2, 1], [2, 1, 5], [2, 3, 9]]
floyd(v, edges)
