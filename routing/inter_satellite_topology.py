from topology_visible_satellite import Visible_Satellite_Topology

cutting_time = "8 Sep 2021 21:18:10"
print(cutting_time)

ft = open("topology_point_statistics.txt", "a+")
ft.writelines(cutting_time + "\n")
ft.close()

list1 = "804 811.0 4714 185    8 Sep 2021 21:13:20    8 Sep 2021 21:31:41"
list2 = "803 665.0 6838 98    8 Sep 2021 21:24:22    8 Sep 2021 21:42:46"

s_satellite_parameter = list1.split("\n")[0]
d_satellite_parameter = list2.split("\n")[0]

ft = open("topology_point_statistics.txt", "a+")
ft.writelines("     " + s_satellite_parameter.split(" ")[0] + "\n")
ft.close()

# call "Visible_Satellite_Topology" to further analyze the visible relationship between satellites
Visible_Satellite_Topology(cutting_time, s_satellite_parameter, d_satellite_parameter)







