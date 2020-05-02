from math import *

print('--------------Exercise 2 Begin----------------')

#1.根据用户输入的华氏度，将其转换为摄氏度
fahrenheit = float(input('Please write the fahrenheit there: '))
centigrade = str(round((fahrenheit-32)/1.8,2))
print('The temperature is '+centigrade+' ℃')

#2.根据用户输入的圆的半径，计算圆的周长和面积
r = float(input('Please write the radius there: '))
L = str(round(2*pi*r,2))
S = str(round(pi*r*r,2))
print('The perimeter of your circle is '+L)
print('The area of your circle is '+S)

#3. 根据用户输入的粉丝量和互动量，计算有效互动比
number_fans = float(input('Please write the number of fans there: '))
number_interaction = float(input('The number of interaction: '))
rate = str(round(number_interaction/number_fans))
print('Efficient interactive rate is '+rate)
print('---------------Exercise 2 End-----------------')