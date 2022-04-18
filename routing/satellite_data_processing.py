# 获取Chain1_Individual_Strand_Access.txt的行数
fp1 = open("Chain1_Individual_Strand_Access.txt")
length = len(fp1.readlines())
fp1.close()

# 整理Chain1_Individual_Strand_Access.txt文件
fp1 = open("Chain1_Individual_Strand_Access.txt")
fp2 = open("satellite_data.txt", "w")

Flag = 0  # 标志位

for i in range(length):
    line = fp1.readline().rstrip()
    if 'Satellite' in line and int(line.split('/')[0].split('e')[2]) > 1:
        Flag = 1
        fp2.writelines(line + "\n")
        continue
    if Flag == 1 and "Sep" in line and "Duration" not in line:
        lines = line.split("                  ")[1].split("           ")[0]
        fp2.writelines(lines.split("    ")[0][:-4] + "     " + lines.split("    ")[1][:-4] + "\n")
        continue

fp1.close()
fp2.close()