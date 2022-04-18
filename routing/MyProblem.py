import numpy as np
import geatpy as ea

class MyProblem(ea.Problem): # 继承Problem父类
    def __init__(self):
        name = 'MyProblem'   # 初始化name（函数名称，可以随意设置）
        M = 1                # 初始化M（目标维数）
        maxormins = [-1]     # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = 3              # 初始化Dim（决策变量维数）
        varTypes = [0] * Dim # 这是一个list,初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [0, 0, 0]       # 决策变量下界
        ub = [1, 1, 1]       # 决策变量上界
        lbin = [0, 0, 0]     # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [0, 0, 0]     # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）

        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)


    def aimFunc(self, pop):      # 目标函数
        Vars = pop.Phen       # 得到决策变量矩阵
        x1 = Vars[:, [0]]     # 取出第一列得到所有个体的x1组成的列向量
        x2 = Vars[:, [1]]     # 第二列
        x3 = Vars[:, [2]]     # 第三列

        fpp = open("maxQi_parameter.txt")
        line = fpp.readline().rstrip().split(" ")
        remaining_time = float(line[0])
        access_time = float(line[1])
        storage_size = float(line[2])
        fpp.close()

        #print(remaining_time)
        #print(access_time)
        #print(storage_size)

        pop.ObjV = remaining_time * x1 + access_time * x2 + storage_size * x3 # 计算目标函数值，赋值给pop种群对象的ObjV属性

        # 采用可行性法则处理约束，numpy的hstack()把x1、x2、x3三个列向量拼成CV矩阵
        pop.CV = np.hstack([x1 - x2, x1 - x3, np.abs(x1 + x2 + x3 - 1)])  #约束条件1，即2*x1 + x2 - 1<= 0或者2*x1 + x2 <= 1,如果是2*x1 + x2 >= 1,则取负写作（-2*x1-x2+1）

