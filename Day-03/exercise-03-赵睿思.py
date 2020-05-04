#华氏温度转换为摄氏温度
fahrenheit = float(input('华氏度为:'))
centigrade = (fahrenheit-32)/1.8
print('转换后的摄氏度值为 '+centigrade)

#计算圆的周长和面积
r = float(input('圆的半径为:'))
Circumference = float(2*pi*r)
Square = float(pi*(r**2))
print('圆的周长为'+Circumference)
print('圆的面积为'+Square)

#计算有效互动比
fans = int(input('粉丝量:'))
interaction = int(input('互动量: '))
proportion = float(interaction/fans)
print('有效互动比为 '+proportion)
