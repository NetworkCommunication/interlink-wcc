from satellite_whether import Data_Normalization_Processing, Selected_Satellite
from MyProblem_solution import Optimization_Model

# 卫星最大服务质量
MAX_Qi_satellite = -9999999

#Flag = 0  # Flag用来标记具有最大服务质量的卫星编号

satellite_four_parameters = ""  # 记录用来标记具有最大服务质量的卫星编号Flag在seleted_satellite.txt中的行数，从而得到所选定卫星的相关属性参数

# 将最终的切换卫星相关参数整合到文件中
fp_last = open("final_selected_satellite.txt", "a")

# 切换时间
cutting_time = "8 Sep 2021 20:46:53"

Selected_Satellite(cutting_time)  # 调用相关函数，得到相应的可选择卫星的数据文件，为接下来选取最优卫星提供数据依据

# 在切换时刻，从所有可选择的能够提供服务的卫星中，选择出具有最大服务质量Qi的卫星
fp1 = open("selected_satellite.txt")
l1 = len(fp1.readlines())
fp1.close()
fp1 = open("selected_satellite.txt")

for i in range(l1):
    line2 = fp1.readline().rstrip()
    line1 = line2.split("    ")[0].split(" ")

    # 调用Optimization_Model函数，计算出每个卫星的服务质量，并加以比较，从而得到具有最优服务质量Qi的卫星(编号)
    data1 = int(float(line1[1]))
    data2 = int(line1[2])
    data3 = int(line1[3])
     # 数据归一化处理
    [data1, data2, data3] = Data_Normalization_Processing(data1, data2, data3)

    fpp = open("maxQi_parameter.txt", "w")
    fpp.writelines(str(data1) + ' ' + str(data2) + ' ' + str(data3))
    fpp.close()

    Qi_satellite = Optimization_Model()
    if Qi_satellite >= MAX_Qi_satellite:
        MAX_Qi_satellite = Qi_satellite
        satellite_four_parameters = line2
    else:
        continue

print("卫星编号和相关参数     " + satellite_four_parameters)
fp_last.writelines("卫星编号和相关参数     " + satellite_four_parameters)

fp1.close()
fp_last.close()
