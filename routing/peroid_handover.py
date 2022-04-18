from satellite_whether import Judge_Time_Size, Remaining_Time, Selected_Satellite_Parameter_Modify, Data_Normalization_Processing
from MyProblem_solution import Optimization_Model

#卫星个数、data_initial_1.txt的行数
NUMBER = 80
#卫星最大访问次数
Max_Access_Time = 7000
#卫星最大存储容量
Max_Storage_Size = 500
#卫星最大服务质量
MAX_Qi_satellite = -9999999

# 获取satellite_start_end_time.txt的行数
fp3 = open("satellite_data.txt")
l3 = len(fp3.readlines())
fp3.close()

#读取当前选择切入的卫星及其相关参数
fp1 = open("final_selected_satellite.txt", "r")
for i in range(2):
    line1 = fp1.readline().rstrip()
    if i == 0:
        current_time = line1.split("          ")[1]
    if i == 1:
        satellite_parameter = line1.split("     ")[1]
fp1.close()

print("   切换时间          " + current_time)
print("卫星编号和相关参数     " + satellite_parameter)

f_handover_statistics = open("handover_satellite_statistics.txt", "w")
f_handover_statistics.writelines(current_time + "\n")
f_handover_statistics.writelines(satellite_parameter + "\n")


#period_segment = [600, 1200, 1800, 2400, 3000, 3600, 4200, 4800, 5400, 6000]
period = 1800   #周期时间段
total_period = period
handover = 0    #切换次数
#handover_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

list = []

while period >= 0:
        period = period - float(satellite_parameter.split("    ")[0].split(" ")[1])
        # 卫星提供完服务后，文件中相应的存储次数和存储容量的修改
        Selected_Satellite_Parameter_Modify(satellite_parameter)
        # 切换次数加1
        handover = handover + 1
        #目前的卫星的服务时间到，切换到下一刻卫星，找寻符合条件的下一颗卫星
        if period < 0:
            break
        fp3 = open("satellite_data.txt")
        fp4_1 = open("seleted_satellite_1.txt", "w")
        l4_1 = 0  # 记录文件seleted_satellite_1.txt的行数
        fp_1 = open("satellite_parameter_initial1.txt")
        # 根据切入时间，选择具有能够接替服务的卫星，并计算出卫星的剩余服务时间、最大剩余访问次数、最大剩余访问容量
        for j in range(0, l3):
            line3 = fp3.readline().rstrip()
            if line3 != '':
                if "Satellite" in line3:
                    Flag = line3.split('/')[0].split('e')[2]  # Flag卫星编号
                    flag = 0
                elif flag == 0:
                    start_time = line3.split("     ")[0]
                    end_time = line3.split("     ")[1]
                    if Judge_Time_Size(start_time, satellite_parameter.rstrip().split("    ")[2], end_time) == 1:
                        # 计算具有接管能力的卫星的相关属性，并将其写入到文件selected_satellite_1.txt中
                        for k in range(NUMBER):
                            line = fp_1.readline().rstrip().split(" ")
                            if line[0] == Flag:
                                line[1] = Remaining_Time(satellite_parameter.rstrip().split("    ")[2], end_time)
                                line[2] = Max_Access_Time - int(line[2])
                                line[3] = Max_Storage_Size - int(line[3])
                                # print(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + " " + str(line[3]) + "    " + start_time + "    " + end_time)
                                fp4_1.writelines(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + " " + str(
                                    line[3]) + "    " + start_time + "    " + end_time + "\n")
                                l4_1 = l4_1 + 1
                                break
                            else:
                                continue
                    else:
                        continue

        fp4_1.close()
        fp3.close()
        fp_1.close()

        MAX_Qi_satellite = -9999999    #卫星最大服务质量

        fp1 = open("seleted_satellite_1.txt")
        for i in range(l4_1):
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

        fp1.close()

        print(satellite_four_parameters)
        list.append(satellite_four_parameters)
        satellite_parameter = satellite_four_parameters

print("相应周期：" + str(total_period))
print("切换次数：" + str(handover))


for i in range(len(list)):
    f_handover_statistics.writelines(list[i] + "\n")

f_handover_statistics.writelines("相应周期：" + str(total_period) + "\n")
f_handover_statistics.writelines("切换次数：" + str(handover))
f_handover_statistics.close()
