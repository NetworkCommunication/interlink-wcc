from satellite_whether import Selected_Satellite
from acquire_satellite_user_location import Acquire_Satellite_User_Location

nearest_location = 99999
satellite_four_parameters = ""

fp_last = open("final_selected_satellite.txt", "a")

cutting_time = "18 Sep 2021 03:00:00"
Selected_Satellite(cutting_time)
fp1 = open("selected_satellite.txt")
l1 = len(fp1.readlines())
fp1.close()
fp1 = open("selected_satellite.txt")

for i in range(l1):
    line2 = fp1.readline().rstrip()
    d = Acquire_Satellite_User_Location(cutting_time, line2)
    if d <= nearest_location:
        nearest_location = d
        satellite_four_parameters = line2
    else:
        continue
print("卫星编号和相关参数     " + satellite_four_parameters)
fp_last.writelines("卫星编号和相关参数     " + satellite_four_parameters)
fp1.close()
fp_last.close()
