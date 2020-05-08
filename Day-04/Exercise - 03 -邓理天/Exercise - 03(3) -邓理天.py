'''
判断是否为质数
'''
num = int(input("请输入一个正整数："))#用户键入数字
i=2 #设定一个用于判断的值
flag = True
while i < num: #循环结构
    if num % i == 0: #分支结构
        flag = False
        break
    else:
        i+=1

if flag: #判断并输出
    print("该数是一个质数")
else:
    print("该数不是一个质数")