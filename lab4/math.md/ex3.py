# дұрыс көпбұрыштың ауданын табу
import math
num_sides = int(input("number of sides: "))
side_length = float(input("length of a side: "))
area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", round(area))
