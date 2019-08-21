from math import radians, cos, sin, asin, sqrt


def geo_distance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371
    return distance


if __name__ == '__main__':
    print(geo_distance(116.716925, 23.361239, 116.721024, 23.363527))
