import random
import time

number = 10
f = open("handover_time.txt", "w")

for i in range(number):
    date1 = (2021, 9, 17, 0, 4, 0, 0, 0, 0)
    date2 = (2021, 9, 18, 0, 3, 0, 0, 0, 0)
    start = time.mktime(date1)
    end = time.mktime(date2)
    t = random.randint(start, end)
    date_touple = time.localtime(t)
    h = time.strftime('%d %b %Y %H:%M:%S', date_touple)
    if int(h.split(':')[0][-2:]) >= 0 and int(h.split(':')[0][-2:]) <= 2:
        h = '18' + h[2:]
    elif int(h.split(':')[0][-2:]) == 3:
        h = '18' + h.split(':')[0][2:] + ':00:00'
    f.writelines(h + "\n")
