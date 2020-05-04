import sys

import math

Radius = float(input('Write the Radius here:'))
Circumference = round(Radius*math.pi,2)
Area = round(Radius*Radius*math.pi,2)
print('The Circumference is',Circumference)
print('The Area is',Area)