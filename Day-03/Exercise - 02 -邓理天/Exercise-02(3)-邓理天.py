'''
计算有效互动比
'''
fans = int(input("请输入粉丝量："))#用户键入粉丝量
interactive = int(input("请输入有效互动量："))#用户键入有效互动量
print('percent: {:.2%}'.format(interactive/fans))#计算输出有效互动百分比
