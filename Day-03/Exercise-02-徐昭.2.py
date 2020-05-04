import math    
R = input("请输入圆的半径(请保留两位小数)：\n")
R = float(R)   
pi = math.pi   
L = 2 * pi * R 
S = R ** 2 * pi  
print ("该圆的周长为{:.2f}，该圆的面积为{:.2f}".format(L,S))  
