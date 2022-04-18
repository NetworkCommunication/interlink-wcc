import time
import random

#Variable initialization
Max_Remaining_Time = 1500
Max_Access_Time = 7000
Max_Storage_Size = 500
Min_Storage_Size = 150
NUMBER = 225

#Determine whether satellites can become alternative satellites when handover occurs
def Judge_Time_Size(start_time, cutting_time, end_time):
    start_time = time.strptime(start_time, '%d %b %Y %H:%M:%S')
    cutting_time = time.strptime(cutting_time, '%d %b %Y %H:%M:%S')
    end_time = time.strptime(end_time, '%d %b %Y %H:%M:%S')
    start_time = time.mktime(start_time)
    cutting_time = time.mktime(cutting_time)
    end_time = time.mktime(end_time)
    if (cutting_time - start_time) > 0 and (end_time - cutting_time) > 0:
        return 1
    else:
        return 0

#Caculation the remaining time of satellites
def Remaining_Time(cutting_time, end_time):
    cutting_time = time.strptime(cutting_time, '%d %b %Y %H:%M:%S')
    end_time = time.strptime(end_time, '%d %b %Y %H:%M:%S')
    cutting_time = time.mktime(cutting_time)
    end_time = time.mktime(end_time)
    return end_time - cutting_time

#Data normalization processing
def Data_Normalization_Processing(remaining_service_time, access_time, storage_size):
    remaining_service_time = (int(remaining_service_time) - 0) / (Max_Remaining_Time - 0)
    access_time = (int(access_time) - 0) / (Max_Access_Time - 0)
    storage_size = abs((int(storage_size) - Min_Storage_Size) / (Max_Storage_Size - Min_Storage_Size))
    return [remaining_service_time, access_time, storage_size]

fp3 = open("stk_data_processing.txt")
l3 = len(fp3.readlines())
fp3.close()
#Problem formulation
def Selected_Satellite():
    fp_last = open("final_selected_satellite.txt", "w")
    fp1 = open("storage_time_initial.txt")
    fp3 = open("stk_data_processing.txt")
    fp4 = open("selected_satellite.txt", "w")
    cutting_time = "18 Sep 2021 03:00:00"
    fp_last.writelines("   切换时间          " + cutting_time + "\n")
    print("切换时间             " + cutting_time)
    Flag_flag = 0
    for i in range(l3):
        line3 = fp3.readline().rstrip()
        if "Satellite" in line3:
            Flag = line3.split('/')[0].split('e')[2]
            flag = 0
        elif flag == 0:
            start_time = line3.split("     ")[0]
            end_time = line3.split("     ")[1]
            if Judge_Time_Size(start_time, cutting_time, end_time) == 1:
                for k in range(NUMBER):
                    line1 = fp1.readline().rstrip().split(" ")
                    if int(line1[0]) == int(Flag):
                        line1[1] = Remaining_Time(cutting_time, end_time)
                        line1[2] = Max_Access_Time - int(line1[2])
                        line1[3] = Max_Storage_Size - int(line1[3])
                        fp4.writelines(str(line1[0]) + " " + str(line1[1]) + " " + str(line1[2]) + " " + str(line1[3]) + "    " + start_time + "    " + end_time + "\n")
                        Flag_flag = 1
                        flag = 1
                        break
                    else:
                        continue
            else:
                continue
    fp1.close()
    fp3.close()
    fp4.close()
    fp_last.close()
    if Flag_flag == 0:
       Selected_Satellite()

#Parameter modify
def Selected_Satellite_Parameter_Modify(satellite_parameter):
    fp_1 = open("storage_time_initial1.txt", "r")
    lines = []
    for line in fp_1.readlines():
        lines.append(line.rstrip())
    fp_1.close()
    for k in range(NUMBER):
        if satellite_parameter.split("    ")[0].split(" ")[0] == lines[k].split(' ')[0]:
            access_time = int(lines[k].split(' ')[2]) + 1
            storage_size = int(lines[k].split(' ')[3]) + random.randint(1, 5)
            lines[k] = lines[k].split(' ')[0] + ' ' + '0' + ' ' + str(access_time) + ' ' + str(storage_size)
            break
        else:
            continue
    fp_1 = open("storage_time_initial1.txt", "w")
    for l in lines:
        fp_1.write(l + '\n')
    fp_1.close()

def Satellite_Visible_Slot_Analysis(cutting_time, visible_slot):
    cutting_time = time.strptime(cutting_time, '%d %b %Y %H:%M:%S')
    cutting_time = time.mktime(cutting_time)
    timeArray = time.localtime(cutting_time + visible_slot)
    cutting_time = time.strftime('%d %b %Y %H:%M:%S', timeArray)
    return cutting_time


