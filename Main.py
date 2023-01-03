#from VRP_Model import Model
from Solver import *
import sol_checker

m = Model()
m.BuildModel()
s = Solver(m)
sol = s.solve()
sol_checker.test_solution('solution.txt', m.allNodes, 14, m.capacity)



