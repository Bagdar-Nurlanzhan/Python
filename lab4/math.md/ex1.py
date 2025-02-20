# радианды градусқа айналдыру
import math
def degree_radian(degree):
    return degree * (math.pi / 180)
degree = float(input())
radian = degree_radian(degree)
print("градус:", round(radian, 6))
