from satellite_whether import Satellite_Visible_Slot_Analysis
from source_destination_satellite_iterative import Source_Destination_Satellite_Iterative
from satellite_whether import Remaining_Time

slot = 200   # 迭代时隙

#搭建卫星可见性拓扑图
def Visible_Satellite_Topology(cutting_time, s_satellite_parameter, d_satellite_parameter):
    Flag = 0
    # 根据时隙，获取下一个切换时刻
    if Remaining_Time(cutting_time, s_satellite_parameter.split("    ")[-1]) < slot:
        end_time = s_satellite_parameter.split("    ")[-1]
        Flag = 1
    else:
        end_time = Satellite_Visible_Slot_Analysis(cutting_time, slot)

    ft = open("topology_point_statistics.txt", "a+")
    ft.writelines(end_time + "\n")
    ft.close()

    s_number = s_satellite_parameter.split(" ")[0]  # 获取源卫星编码
    filename = "v" + s_number + ".txt"        # 得到源卫星对其他卫星可见性的文件

    # 得到在当前时隙的切换时刻，源卫星可见的目标卫星列表
    list = Source_Destination_Satellite_Iterative(filename, cutting_time, end_time)

    ft = open("topology_point_statistics.txt", "a+")
    ft.writelines("     " + s_number + ":" + ','.join(list) + "\n")
    ft.close()

    if Flag == 0:
        Iteration(list, end_time, s_satellite_parameter, d_satellite_parameter)


# 时隙内，卫星间可见性迭代分析
def Iteration(list, cutting_time, s_satellite_parameter, d_satellite_parameter):
    # 可见卫星列表初始化
    final_list = []

    l = len(list)
    tt = Satellite_Visible_Slot_Analysis(cutting_time, slot)  # 获取该时隙内的下一个切换时刻

    ft = open("topology_point_statistics.txt", "a+")
    ft.writelines(tt + "\n")
    ft.close()

    for i in range(l):
        filename = "v" + list[i] + ".txt"
        target_list = Source_Destination_Satellite_Iterative(filename, cutting_time, tt)

        for j in range(len(target_list)):
            final_list.append(target_list[j])

        ft = open("topology_point_statistics.txt", "a+")
        ft.writelines("     " + list[i] + ":")
        ft.writelines(','.join(target_list) + "\n")
        ft.close()

    # final_list去重
    news_final_list = []
    for id in final_list:
        if id not in news_final_list:
            news_final_list.append(id)

    # 计算最后划分时隙后，不足的数据
    remain_t = Remaining_Time(tt, s_satellite_parameter.split("    ")[-1])
    if remain_t > slot:
        Iteration(news_final_list, tt, s_satellite_parameter, d_satellite_parameter)
    else:
        l = len(news_final_list)
        tt = Satellite_Visible_Slot_Analysis(tt, remain_t)  # 获取该时隙内的下一个切换时刻

        ft = open("topology_point_statistics.txt", "a+")
        ft.writelines(tt + "\n")
        ft.close()

        for i in range(l):
            filename = "v" + final_list[i] + ".txt"
            target_list = Source_Destination_Satellite_Iterative(filename, cutting_time, tt)

            ft = open("topology_point_statistics.txt", "a+")
            ft.writelines("     " + news_final_list[i] + ":")
            ft.writelines(','.join(target_list) + "\n")
            ft.close()

