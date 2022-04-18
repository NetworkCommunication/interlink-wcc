'''
    Custom Question.
'''

import numpy as np
import geatpy as ea

class MyProblem(ea.Problem):
    def __init__(self):
        name = 'MyProblem'
        M = 1                # initialize target dimension
        maxormins = [-1]     # initialize maxormins(maximize)
        Dim = 3
        varTypes = [0] * Dim
        lb = [0, 0, 0]       # Lower bound of decision variable
        ub = [1, 1, 1]       # Upper bound of decision variable
        lbin = [0, 0, 0]     # Lower boundary of decision variable
        ubin = [0, 0, 0]     # Upper boundary of decision variable

        # Call the parent class constructor to complete instantiation
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):      # target function
        Vars = pop.Phen       # decision variable matrix
        x1 = Vars[:, [0]]
        x2 = Vars[:, [1]]
        x3 = Vars[:, [2]]

        fpp = open("maxQi_parameter.txt")
        line = fpp.readline().rstrip().split(" ")
        remaining_time = float(line[0])
        access_time = float(line[1])
        storage_size = float(line[2])
        fpp.close()

        pop.ObjV = remaining_time * x1 + access_time * x2 + storage_size * x3    # calculate objective function value
        pop.CV = np.hstack([x1 - x2, x1 - x3, np.abs(x1 + x2 + x3 - 1)])  # constraint condition

