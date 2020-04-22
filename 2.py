from scipy.optimize import linprog
import numpy as np
print("Введите количество строк матрицы H:")
n = int(input())
H = []
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
if(a == b):
    print("Разрешима в чистых стратегиях!")
else:
    print("Не разрешима в чистых стратегиях.")
x = [1 for i in range(n)]
a_ = np.array(H).transpose()*(-1)
b_ = [-1 for i in range(len(H[0]))]
print("Оптимальные решения: ")
x_solve = linprog(x, a_, b_).x
print ("x = ", x_solve)
y = [-1 for i in range(len(H[0]))]
a_ = H
b_ = [1 for i in range(n)]
y_solve = linprog(y, a_, b_).x
print("y =", y_solve)
I = 1/sum(y_solve)
print ("I = :", I)
print("Оптимальные смешанные стратегии:")
p = [I*variable for variable in x_solve]
print("p =", p)
q = [I*variable for variable in y_solve]
print("q =", q)
