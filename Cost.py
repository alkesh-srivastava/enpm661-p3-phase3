import matplotlib.pyplot as plt
import random
import math

def roundingpoint(point):
    # It rounds the floating point number to a float point of 3 significant figure after decimal.

    if point[0].is_integer() and point[1].is_integer() or (point[0] - 0.5).is_integer() and (
            point[1] - 0.5).is_integer():
        return point
    else:
        new_point = (round(point[0] * 8) / 8, round(point[1] * 8) / 8)
        return new_point


def cost(Xi, Yi, Thetai, UL, UR):
    t = 0
    r = 0.038
    L = 0.354
    dt = 0.1
    Xn = Xi
    Yn = Yi
    Thetan = 3.14 * Thetai / 180

    # Xi, Yi,Thetai: Input point's coordinates
    # Xs, Ys: Start point coordinates for plot function
    # Xn, Yn, Thetan: End point coordintes


    D = 0
    while t < 1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5 * r * (UL + UR) * math.cos(Thetan) * dt
        Xn = round(Xn * 32) / 32
        Yn += 0.5 * r * (UL + UR) * math.sin(Thetan) * dt
        Yn = round(Yn * 32) / 32
        Thetan += (r / L) * (UR - UL) * dt
        # Thetan = round(Thetan * 8) / 8
        D = D + math.sqrt(math.pow((0.5 * r * (UL + UR) * math.cos(Thetan) * dt), 2) + math.pow(
            (0.5 * r * (UL + UR) * math.sin(Thetan) * dt), 2))
        # D = round(D * 8) / 8
    Thetan = 180 * (Thetan) / 3.14
    Thetan = round(Thetan * 8) / 8
    tup_return = (Xn, Yn, Thetan, D, UL, UR)
    return tup_return
