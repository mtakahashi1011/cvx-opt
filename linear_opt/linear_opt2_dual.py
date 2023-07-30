from pulp import *
import numpy as np 
A = np.array([[3, 1, 2], [1, 3, 0], [0, 2, 4]])
c = np.array([150, 200, 300])
b = np.array([60, 36, 48])
(m, n) = A.shape
AT = A.T
dual = LpProblem(name='Dual_Production', sense=LpMinimize)
y = [LpVariable('y'+str(i+1), lowBound=0) for i in range(m)]
dual += lpDot(b, y)
for j in range(n):
    dual += lpDot(AT[j], y) >= c[j], 'ineq'+str(j+1)
dual.solve()
print(LpStatus[dual.status])
print('Optimal value of dual problem =', value(dual.objective))
for v in dual.variables():
    print(v.name, '=', v.varValue)
Y = np.array([v.varValue for v in dual.variables()])
print(np.dot(AT, Y) - c)
print(np.all(np.dot(AT, Y) - c >= -1.0e-5))
