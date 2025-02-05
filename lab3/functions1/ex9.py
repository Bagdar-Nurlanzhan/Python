import math
def sphere_volume(radius):
    if radius < 0:
        return "not negative values"
    volume = (4/3) * math.pi * radius**3
    return volume
radius = float(input())
print(sphere_volume(radius))
