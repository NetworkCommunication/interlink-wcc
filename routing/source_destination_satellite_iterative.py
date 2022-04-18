from satellite_whether import Remaining_Time

# 在迭代过程中，源卫星和暂时目的卫星之间的可见性分析，得到在当前状态下，目的卫星列表list[]
def Source_Destination_Satellite_Iterative(file_name, cutting_time, iterative_time):
    f = open(file_name)
    l = len(f.readlines())
    f.close()

    Flag = 0  # 标志位
    list = [] # 用来存储与源卫星可见的其他卫星编号
    f = open(file_name)
    for i in range(l):
        line = f.readline().rstrip()
        if 'Satellite' in line:
            Flag = 1
            target_satellite = line[-3:]  # 当前时隙的目标卫星
            # 判断在当前切换时刻和时隙结束时刻，其他卫星是否与源卫星可见
        if Flag == 1 and "Sep" in line and "Duration" not in line:
            #print(line[28:78].split("    ")[0][:-4])  # 开始时间
            #print(line[28:78].split("    ")[1][:-4])  # 结束时间
            # 计算其他卫星的开始时间和结束时间，是否满足当前切换时刻和时隙结束时刻的需要，如果满足，将该其他卫星添加到列表list[]中
            if Remaining_Time(line[28:78].split("    ")[0][:-4], cutting_time) >= 0 and Remaining_Time(iterative_time, line[28:78].split("    ")[1][:-4]) >= 0:
                if target_satellite in list:
                    continue
                else:
                    list.append(target_satellite)   # 将当前时隙的目标卫星添加到列表中
            else:
                continue
    f.close()
    return list
