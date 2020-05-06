'''
判断是否为互质数
'''
a = int(input("请输入第一个正整数："))
b = int(input("请输入第二个正整数："))#用户键入数字
while b!=0:#用连续求商法
    temp = a % b
    a = b
    b = temp
if a == 1:  #判断并输出结果
    print("您输入的两个数为互质数")
else:
    print("您输入的两个数不是互质数")