import random
import numpy as np

#卫星个数15*15
NUMBER = 80

#卫星编号和属性初始化函数
def Satellite_Parameter_Initial():
    # 卫星数组：第一个参数表示卫星编号，第二个参数表示卫星剩余服务时间，第三个参数表示卫星访问次数，第四个参数表示卫星存储容量
    satellite = np.zeros((NUMBER, 4))
    # 卫星数据初始化
    k = 1
    h = 1
    for i in range(NUMBER):
        if (i != 0 and i % 10 == 0):
            k += 1
            h = 1
        satellite[i][0] = 100 * k + h
        satellite[i][2] = random.randint(0, 7000)
        satellite[i][3] = random.randint(150, 500)
        h += 1
    # print(satellite)

    # 将卫星数据保存到文件中
    np.savetxt("satellite_parameter_initial.txt", satellite, fmt="%d", delimiter=" ")
    np.savetxt("satellite_parameter_initial1.txt", satellite, fmt="%d", delimiter=" ")

Satellite_Parameter_Initial()


