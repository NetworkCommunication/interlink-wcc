from source_destination_satellite_iterative import Source_Destination_Satellite_Iterative
from satellite_whether import Satellite_Visible_Slot_Analysis

slot = 10   # 迭代时隙

def Iteration(list, cutting_time):
    # 可见卫星列表初始化
    final_list = []

    print(cutting_time)
    l = len(list)
    tt = Satellite_Visible_Slot_Analysis(cutting_time, 10)
    print(tt)

    ft = open("topology_point_statistics.txt", "a+")
    ft.writelines(tt + "\n")
    #ft.writelines("     " + ','.join(list) + "\n")
    ft.close()

    for i in range(l):
        filename = "v" + list[i] + ".txt"
        target_list = Source_Destination_Satellite_Iterative(filename, cutting_time, tt)
        print(target_list)

        for j in range(len(target_list)):
            final_list.append(target_list[j])

        ft = open("topology_point_statistics.txt", "a+")
        ft.writelines("     " + list[i] + ":")
        ft.writelines(','.join(target_list) + "\n")
        ft.close()
    print(final_list)

    Iteration(final_list, tt)

#Iteration(['106', '107', '108', '205', '206', '207', '304', '306', '403', '404', '405', '503', '504', '505'], "9 Sep 2021 00:38:06")




