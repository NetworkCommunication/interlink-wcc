import random
import time

#实验次数
number = 10

#将所有切换时间保存到文件中
f = open("handover_time.txt", "w")

#随机生成最初的卫星切换时刻
for i in range(number):
    # 给定STK仿真的开始时间和结束时间,考虑到实验最长时长为3000s，所以生成的最晚的随机时间为2021-9-9 03：00：00
    date1 = (2021, 9, 8, 0, 4, 0, 0, 0, 0)  # 设置开始日期时间元组（2021-9-8 04：00：00）
    date2 = (2021, 9, 9, 0, 3, 0, 0, 0, 0)  # 设置结束日期时间元组（2021-9-9 03：00：00）

    start = time.mktime(date1)  # 生成开始时间戳
    end = time.mktime(date2)  # 生成结束时间戳

    # 生成选取实验次数的开始切入时间，并将其保存到文件中

    # 在开始时间和结束时间之间随机生成一个日期
    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组

    # 将时间元组转换成文本中的格式，24 Apr 2021 04:12:34
    h = time.strftime('%d %b %Y %H:%M:%S', date_touple)

    # 判断时间是否为凌晨00：00：00-03：00：00，如果是的话，修改日期为25 Apr 2021
    if int(h.split(':')[0][-2:]) >= 0 and int(h.split(':')[0][-2:]) <= 2:
        h = '9' + h[2:]
    elif int(h.split(':')[0][-2:]) == 3:
        h = h.split(':')[0] + ':00:00'
    else:
        h = h[1:]

    f.writelines(h + "\n")
