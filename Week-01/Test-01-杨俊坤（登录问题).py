def Log_in(用户名,密码):         #定义函数
    默认用户名= "NealPayne"
    默认密码 = "NealPayne"
    if 用户名==默认用户名 and 密码==默认密码:      #循环语句
        return True
    else:
        return  False
for Z in range(0,3):                                           #range循环
    X = input('请输入你的用户名：')
    Y = input('请输入你的密码：')
    if Log_in(X,Y)==True:                             #调用函数
        print('登陆成功')
        break
    else:
        print('用户名或密码错误，若连续3次错误则自动锁死账号')
        if Z == 2:
            print('因连续3次输入用户名或密码错误，账号已锁死')
