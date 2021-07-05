import math


def find_nb(m):
    n = 0
    current_cube_vol = 0
    while True:
        if m > 0:
            current_cube_vol = math.pow(n + 1, 3)
            m = m - current_cube_vol
        elif m == 0:
            return n
        elif m < 0:
            return -1
        n += 1


find_nb(1071225)