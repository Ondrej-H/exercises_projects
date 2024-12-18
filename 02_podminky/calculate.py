from math import pi

def cube_calc_volume(a):
    volume = a**3
    return volume


def cuboid_calc_volume(a,b,c):
    volume = a*b*c
    return volume


def sphere_calc_volume(r):
    volume = 4/3 * pi * r**3
    return volume


def cube_calc_surface(a):
    surface = 6 * a**2
    return surface


def cuboid_calc_surface(a,b,c):
    surface = 2 * (a*b + a*c + b*c)
    return surface


def sphere_calc_surface(r):
    surface = 4 * pi * r**2
    return surface

