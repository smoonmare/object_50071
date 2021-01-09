import math

length_ab = int(input())
length_bc = int(input())
angle = round(math.degrees(math.atan(length_ab / length_bc)))
print(angle, chr(176), sep='')