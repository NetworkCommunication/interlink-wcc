from satellite_whether import Selected_Satellite

Min_Remaining_Time = 99999
Min_str = ""
sum_probability = 0.0
satellite_four_parameters = ""

fp_last = open("final_selected_satellite.txt", "a")
cutting_time = "18 Sep 2021 01:00:00"
Selected_Satellite(cutting_time)

fp1 = open("selected_satellite.txt")
l1 = len(fp1.readlines())
fp1.close()
fp1 = open("selected_satellite.txt")
for i in range(l1):
    line2 = fp1.readline().rstrip()
    line1 = line2.split("    ")[0].split(" ")
    remaining_time = int(float(line1[1]))
    if remaining_time <= Min_Remaining_Time:
            Min_Remaining_Time = remaining_time
            satellite_four_parameters = line2
    else:
        continue
print("卫星编号和相关参数     " + satellite_four_parameters)
fp_last.writelines("卫星编号和相关参数     " + satellite_four_parameters)
fp1.close()
fp_last.close()
