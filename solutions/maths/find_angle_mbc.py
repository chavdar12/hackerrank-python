from math import atan2, degrees


def angle_mbc(ab, bc):
    return f"{round(degrees(atan2(ab, bc)))}\N{DEGREE SIGN}"
