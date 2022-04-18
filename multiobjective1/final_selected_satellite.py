from satellite_whether import Data_Normalization_Processing, Selected_Satellite
from MyProblem_solution import Optimization_Model

MAX_Qi_satellite = -9999999
satellite_four_parameters = ""
fp_last = open("final_selected_satellite.txt", "a")
Selected_Satellite()

fp1 = open("selected_satellite.txt")
l1 = len(fp1.readlines())
fp1.close()

'''select the most optimal candidate satellite'''
fp1 = open("selected_satellite.txt")
for i in range(l1):
    line2 = fp1.readline().rstrip()
    line1 = line2.split("    ")[0].split(" ")

    data1 = int(float(line1[1]))
    data2 = int(line1[2])
    data3 = int(line1[3])

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
