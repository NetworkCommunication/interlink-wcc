from numpy import *

def Acquire_Satellite_User_Location(time, line):
    number = line.split("    ")[0].split(" ")[0]
    if len(number) <= 3:
        number = '0' + number
    filename = 'Satellite' + number + "_J2000_Position_Velocity.csv"
    f = open(filename, "r")
    l = len(f.readlines())
    f.close()

    x1 = -2623.915544
    y1 = 3974.427442
    z1 = 4228.468237

    f = open(filename, "r")
    for i in range(l):
        lines = f.readline().rstrip()
        if time[:-3] == lines.split(",")[0][:-7]:
            x = float(lines.split(",")[1]) + int(time[18:]) * float(lines.split(",")[4])
            y = float(lines.split(",")[2]) + int(time[18:]) * float(lines.split(",")[5])
            z = float(lines.split(",")[3]) + int(time[18:]) * float(lines.split(",")[6])
            d = sqrt((x-x1)*(x-x1) + (y-y1)*(y-y1) + (z-z1)*(z-z1))
            return d
