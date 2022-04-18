import numpy as np
import geatpy as ea
from MyProblem import MyProblem

def Optimization_Model():
    try:
        problem = MyProblem()
        Encoding = 'RI'
        NIND = 100
        Field = ea.crtfld(Encoding, problem.varTypes, problem.ranges, problem.borders)
        population = ea.Population(Encoding, Field, NIND)
        myAlgorithm = ea.soea_SGA_templet(problem, population)
        myAlgorithm.MAXGEN = 500
        myAlgorithm.drawing = 0

        [population, obj_trace, var_trace] = myAlgorithm.run()
        population.save()
        best_gen = np.argmin(problem.maxormins * obj_trace[:, 1])
        best_ObjV = obj_trace[best_gen, 1]
    except RuntimeError:
        return 0
    else:
        return best_ObjV

