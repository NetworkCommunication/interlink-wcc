'''
    select all valid routing based on fixed time slots,
    as for the continuous visibility between satellites,
    it need to further analyze the satellite data obtained by STK.
'''

import numpy as np
from a_wcc import A_WCC

NUMBER = 80

def Path_Finding(matrix):
    s_s = '804'      # source satellite number
    d_s = 803      # destination satellite number
    list_s = []
    list = []
    list_s.append(int(s_s))  # store all valid routings

    row = (int(s_s[0]) - 1) * 10 + (int(s_s[1:]) - 1)

    for i in range(80):
        if 1 in matrix[row][i]:
            if i <= 9:
                number = 101 + i
            else:
                number = (int(str(i)[0]) + 1) * 100 + i % 10 + 1
            list_s.append(number)
            for j in range(80):
                if 2 in matrix[i][j]:
                    if j <= 9:
                        number = 101 + j
                    else:
                        number = (int(str(j)[0]) + 1) * 100 + j % 10 + 1
                    list_s.append(number)
                    for k in range(80):
                        if 3 in matrix[j][k]:
                            if k <= 9:
                                number = 101 + k
                            else:
                                number = (int(str(k)[0]) + 1) * 100 + k % 10 + 1
                            if number == d_s:
                                list_s.append(number)
                                list.append(list_s)
                                list_s = list_s[0:-1]
                                break
                            else:
                                continue
                    if list_s[-1] == d_s:
                        list.append(list_s)
                    list_s = list_s[0:-1]
            if list_s[-1] == d_s:
                list.append(list_s)
            list_s = list_s[0:-1]
    ll_list = []
    for m in range(len(list)):
        if len(list[m]) == 4 and len(list[m]) == len(set(list[m])):
            ll_list.append(list[m])
    print(A_WCC(ll_list))

def Path_Graph():
    flag = 0
    matrix = np.zeros((80, 80), dtype=list)
    for i in range(80):
        for j in range(80):
            matrix[i][j] = [0]
    f = open("topology_point_statistics.txt", "r")
    l = len(f.readlines())
    f.close()
    f = open("topology_point_statistics.txt", "r")
    for i in range(l):
        lines = f.readline().rstrip()
        if 'Sep' in lines:
            now_time = lines
            flag += 1
        elif 'Sep' not in lines and ':' in lines:
            s_satellite = lines.split("     ")[1].split(":")[0]
            d_list = lines.split("     ")[1].split(":")[1].split(",")
            matrix_row = (int(s_satellite[0]) - 1) * 10 + (int(s_satellite[1:]) - 1)
            matrix_column = []
            for j in range(len(d_list)):
                matrix_column.append((int(d_list[j][0]) - 1) * 10 + int(d_list[j][1:]) - 1)
            for k in range(len(matrix_column)):
                matrix[matrix_row][matrix_column[k]].append(flag)
    f.close()
    Path_Finding(matrix)
Path_Graph()


