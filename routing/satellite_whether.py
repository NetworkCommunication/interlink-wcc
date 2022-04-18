import time
import random

#卫星最大覆盖时间【0，1500】
Max_Remaining_Time = 1500
#卫星最大访问次数【0，7000】
Max_Access_Time = 7000
#卫星最大/小存储容量【150G，500G】
Max_Storage_Size = 500
Min_Storage_Size = 150
#卫星个数、satellite-data.txt文件的行数、、data_initial_1.txt的行数
NUMBER = 80

#判定在切入时刻，其他卫星能否进行切换
#给定日期时间格式，生成相应的时间戳，判断时间大小
def Judge_Time_Size(start_time, cutting_time, end_time):

    # 将字符串形式的时间转换为时间元组
    start_time = time.strptime(start_time, '%d %b %Y %H:%M:%S')
    cutting_time = time.strptime(cutting_time, '%d %b %Y %H:%M:%S')
    end_time = time.strptime(end_time, '%d %b %Y %H:%M:%S')

    # 将时间元组转换为时间戳
    start_time = time.mktime(start_time)
    cutting_time = time.mktime(cutting_time)
    end_time = time.mktime(end_time)

    #判断当前切换时间，有那颗卫星能够接替提供服务
    if (cutting_time - start_time) > 0 and (end_time - cutting_time) > 0:
        return 1
    else:
        return 0


#计算卫星的剩余服务时间
def Remaining_Time(cutting_time, end_time):

    # 将字符串形式的时间转换为时间元组
    cutting_time = time.strptime(cutting_time, '%d %b %Y %H:%M:%S')
    end_time = time.strptime(end_time, '%d %b %Y %H:%M:%S')
    # 将时间元组转换为时间戳
    cutting_time = time.mktime(cutting_time)
    end_time = time.mktime(end_time)
    # 返回卫星的剩余服务时间
    return end_time - cutting_time


#数据归一化处理
def Data_Normalization_Processing(remaining_service_time, access_time, storage_size):
    remaining_service_time = (int(remaining_service_time) - 0) / (Max_Remaining_Time - 0)
    access_time = (int(access_time) - 0) / (Max_Access_Time - 0)
    storage_size = abs((int(storage_size) - Min_Storage_Size) / (Max_Storage_Size - Min_Storage_Size))

    return [remaining_service_time, access_time, storage_size]

# 获取satellite_start_end_time.txt的行数
fp3 = open("satellite_data.txt")
l3 = len(fp3.readlines())
fp3.close()


#问题建模
#根据相应的切换时间，计算出在该切换时间下,都有哪些卫星可以提供服务，然后进一步计算这些可以提供服务的卫星的最大服务质量Qi
def Selected_Satellite(cutting_time):
    fp_last = open("final_selected_satellite.txt", "w")  # 将最终的切换卫星相关参数整合到文件中
    fp1 = open("satellite_parameter_initial.txt")
    fp3 = open("satellite_data.txt")
    fp4 = open("selected_satellite.txt", "w")

    #Data_Initial()  # 卫星相关属性的生成：编号、剩余服务时间、访问次数、存储容量

    #cutting_time = "9 Sep 2021 00:37:46"  # 获得当前切换时间
    fp_last.writelines("   切换时间          " + cutting_time + "\n")
    print("切换时间             " + cutting_time)
    # 标志位，用来判断在当前时刻，是否存在可切换的卫星，如果存在Flag_flag = 1；否则，Flag_flag = 0
    Flag_flag = 0
    # 根据切入时间，选择具有能够接替服务的卫星，并计算出卫星的剩余服务时间、最大剩余访问次数、最大剩余访问容量
    for i in range(l3):
        line3 = fp3.readline().rstrip()
        if "Satellite" in line3:
            Flag = line3.split('/')[0].split('e')[2]  # Flag卫星编号
            flag = 0
        elif flag == 0:
            start_time = line3.split("     ")[0]
            end_time = line3.split("     ")[1]
            if Judge_Time_Size(start_time, cutting_time, end_time) == 1:
                # 计算具有接管能力的卫星的相关属性，并将其写入到文件seleted_satellite.txt中
                for k in range(NUMBER):
                    line1 = fp1.readline().rstrip().split(" ")
                    if line1[0] == Flag:
                        line1[1] = Remaining_Time(cutting_time, end_time)
                        line1[2] = Max_Access_Time - int(line1[2])
                        line1[3] = Max_Storage_Size - int(line1[3])
                        #print(str(line1[0]) + " " + str(line1[1]) + " " + str(line1[2]) + " " + str(line1[3]) + "    " + start_time + "    " + end_time)
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


# 卫星提供完服务后，相应的参数修改
def Selected_Satellite_Parameter_Modify(satellite_parameter):
    # 将原始数据文件读取到列表中，为后期修改做准备
    fp_1 = open("satellite_parameter_initial1.txt", "r")
    lines = []  # 创建了一个空列表，里面没有元素
    for line in fp_1.readlines():
        lines.append(line.rstrip())
    fp_1.close()

    # 当前卫星服务时间到，修改“data_initial_1.txt"文件中其对应的访问次数和存储容量
    for k in range(NUMBER):
        if satellite_parameter.split("    ")[0].split(" ")[0] == lines[k].split(' ')[0]:
            access_time = int(lines[k].split(' ')[2]) + 1  # 访问次数加一
            storage_size = int(lines[k].split(' ')[3]) + random.randint(1, 5)  # 存储容量增加1G-5G大小
            lines[k] = lines[k].split(' ')[0] + ' ' + '0' + ' ' + str(access_time) + ' ' + str(storage_size)
            #print(lines[k])
            break
        else:
            continue

    # 在文件中修改选中卫星提供服务后的访问次数和存储容量
    fp_1 = open("data_initial_1.txt", "w")
    for l in lines:
        fp_1.write(l + '\n')
    fp_1.close()


# 根据原来的字符串时间和相应的时隙，得到新的字符串时间
def Satellite_Visible_Slot_Analysis(cutting_time, visible_slot):
    # 将字符串形式的时间转换为时间元组
    cutting_time = time.strptime(cutting_time, '%d %b %Y %H:%M:%S')
    # 将时间元组转换为时间戳
    cutting_time = time.mktime(cutting_time)
    # 将时间戳转换成时间元组
    timeArray = time.localtime(cutting_time + visible_slot)
    # 将时间元组转换成字符串形式
    cutting_time = time.strftime('%d %b %Y %H:%M:%S', timeArray)
    return cutting_time


