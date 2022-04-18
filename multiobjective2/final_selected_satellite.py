from satellite_whether import Data_Normalization_Processing, Selected_Satellite
from MyProblem_solution import Optimization_Model
from service_user_number import Service_User_Number
import random

MAX_Qi_satellite = -9999999
satellite_four_parameters = ""

fp_last = open("final_selected_satellite.txt", "a")

cutting_time = "18 Sep 2021 02:00:00"
Selected_Satellite(cutting_time)

fp1 = open("selected_satellite.txt")
l1 = len(fp1.readlines())
fp1.close()

fp1 = open("selected_satellite.txt")
if l1 == 1:
    satellite_four_parameters = fp1.readline().rstrip()
else:
    for i in range(l1):
        line2 = fp1.readline().rstrip()
        line1 = line2.split("    ")[0].split(" ")
        number = Service_User_Number(cutting_time, line2)   # judge the influence of other users
        if number == 0:
            number = 20
        data1 = int(float(line1[1])) * (1 - random.randint(1, number) / 20)
        data2 = int(line1[2]) - 200 * random.randint(1, number)
        data3 = int(line1[3]) - 10 * random.randint(1, number)
        [data1, data2, data3] = Data_Normalization_Processing(data1, data2, data3)  # data normalization

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
