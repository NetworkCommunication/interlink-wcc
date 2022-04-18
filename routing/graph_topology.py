from draw_point import DrawPoint

f = open("topology_point_statistics.txt", "r")
l = len(f.readlines())
f.close()

f = open("topology_point_statistics.txt", "r")
for i in range(l):
    lines = f.readline().rstrip()

    if 'Sep' in lines:
        now_time = lines
    elif 'Sep' not in lines and ':' in lines:
        s_satellite = lines.split("     ")[1].split(":")[0]  # 存储源卫星
        d_list = lines.split("     ")[1].split(":")[1].split(",")  # 存储目的卫星列表

        print(s_satellite)
        print(d_list)
        # 将得到的源卫星和目标卫星进行点绘制，并将相对应的编号进行连接，构图
        DrawPoint(s_satellite, d_list, now_time)
        break
    else:
        continue









