'''
逗号分隔列表元素
'''
list = [input("请输入列表:")]#用户键入列表
a = len(list)#获取列表长度
for i in range(a):#输出用逗号隔开的每个元素
    if i < a-1:
        print(list[i]+',')
    else:
        print(list[i]+' ')