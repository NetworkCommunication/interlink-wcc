from math import sin, asin, cos, radians, fabs, sqrt

EARTH_RADIUS = 6371  # 地球平均半径，6371km


def hav(theta):
    s = sin(theta / 2)
    return s * s


def get_distance_hav(lat0, lng0, lat1, lng1):
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance


#lon1, lat1 = (22.599578, 113.973129)  # 深圳野生动物园(起点）
#lon2, lat2 = (22.6986848, 114.3311032)  # 深圳坪山站 (百度地图测距：38.3km)
#d2 = get_distance_hav(lon1, lat1, lon2, lat2)
#print(d2)
