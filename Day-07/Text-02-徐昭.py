import math
t1 = (10 * 22 - 16 * 10) / (22 - 10) #计算出草的生长速度为5
t2 = 10 * 22 - t1 * 22 #计算出原有草量为110
t3 = int(input ("请输入您想喂的牛头数，以便我们为您计算草场可供吃的天数："))
t4 = t2 / (t3 - t1)
if t4 < 1:
    print ("少喂点牛吧，草不够吃一天啦！")
else:
    print("如果您喂%d头牛，草场可供吃%s天"%(t3,t4))
