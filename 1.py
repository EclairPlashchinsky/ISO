from pulp import *
print ("Сколько работников нужно с 2 до 6?")
from2to6 = input()
print ("Сколько работников нужно с 6 до 10?")
from6to10 = input()
print ("Сколько работников нужно с 10 до 14?")
from10to14 = input()
print ("Сколько работников нужно с 14 до 18?")
from14to18 = input()
print ("Сколько работников нужно с 18 до 22?")
from18to22 = input()
print ("Сколько работников нужно с 22 до 2?")
from22to2 = input()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)
x6 = pulp.LpVariable("x6", lowBound=0)
problem = pulp.LpProblem("0", LpMinimize)
problem += x6, "Функция цели"
problem += x6 + x1 >= int(from2to6), "1"
problem += x1 + x2 >= int(from6to10), "2"
problem += x2 + x3 >= int(from10to14), "3"
problem += x3 + x4 >= int(from14to18), "4"
problem += x4 + x5 >= int(from18to22), "5"
problem += x5 + x6 >= int(from22to2), "6"
problem.solve()
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Значение целевой функции:", value(problem.objective))
