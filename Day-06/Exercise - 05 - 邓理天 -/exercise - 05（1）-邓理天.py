'''
将计算有效互动比的方法写为函数并调用
'''

def rate(m,n):#计算比例的函数
    a = n / m
    return a

fans = int(input("请输入粉丝量："))#用户键入粉丝量
interactive = int(input("请输入有效互动量："))#用户键入有效互动量
r = rate(fans,interactive)
print('percent: {:.2%}'.format(r))#计算输出有效互动百分比