'''
计算圆的周长和面积
'''
import math #导入math模块
r = float(input("请输入圆的半径（单位cm)：")) #用户键入半径值
C = 2*math.pi*r #计算周长
S = math.pi*r**2 #计算面积
print("该圆的周长为：",C,"cm","该圆的面积为：",S,"cm²")
