import numpy as np
import nashpy as nash
import re
import matplotlib.pyplot as plt

print("Введите количество строк матрицы H")
n = int(input())
H = []
row_del = []
col_del = []
for_I = []
for_J = []

for i in range(n):
    print("Введите элементы " + str(i+1) + " строки через пробел:")
    row = input().split()
    for i in range(len(row)):
        row[i] = int(row[i])
    H.append(row)

alpha1 = min(H[0])
alpha2 = 0
a = alpha1
for i in range(n):
    alpha2 = min(H[i])
    if(alpha2 > alpha1):
        a = alpha2
        
h = np.array(H)
beta1 = max(h[:,0])
beta2 = 0
b = beta1
for i in range(len(H[0])):
    beta2 = max(h[:,i])
    if(beta2 < beta1):
        b = beta2
        
print("a = ", a)
print("b = ", b)

H_np = np.array(H)
rps = nash.Game(H_np)
equilibria = rps.support_enumeration()
string = str(list(equilibria))
variance = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',string)
p = variance[:n]
print("p =",p)
q = variance[n:(len(H[0]) + n)]
print("q =",q)

for i in range(len(p)):
    if p[i] == '0.':
        row_del.append(i)
    else:
        for_I.append(int(i))
for j in range(len(q)):
    if q[j] == '0.':
        col_del.append(j)
    else:
        for_J.append(int(j))
row_del = row_del[::-1]
col_del = col_del[::-1]
for row in row_del:
    H_np  = np.delete(H_np, row, axis=0)
for col in col_del:
    H_np  = np.delete(H_np, col, axis=1)
I = 0.
H_np_trans = H_np.transpose()
for i in range(len(H_np_trans[0])):
    I = I + H_np_trans[0][i]*float(p[for_I[i]])
print("I = ", I)
H_np_trans = H_np.transpose()
plt.plot([0,1],[H_np[1][0], H_np[0][0]],[0,1],[H_np[1][1], H_np[0][1]])
plt.xlim(0,1)
plt.title("Первый игрок")

plt.show()

plt.plot([0,1],[H_np[0][1], H_np[0][0]],[0,1],[H_np[1][1], H_np[1][0]])
plt.xlim(0,1)
plt.title("Второй игрок")

plt.show()
