'''
返回文件后缀名
'''
filename = input("请输入文件名：")#用户键入文件名
a = filename.find(".") + 1#获取分隔符.的位置
print(filename[a:])#输出.后的文件后缀名