print("请输入以下信息，进行用户注册")
name = input("请输入用户名：")
word = input("请输入密码：")
print("注册成功。请登录账户：")
x = True
count = 1
while  x :
    usersname = input("请输入用户名：")
    password = input("请输入密码：")

    if count==3:
        print("因连续3次输入用户名或密码错误，账号已锁死")
        break
    if count<3:
        if usersname==name and password==word:
            print("登陆成功")
            break
        else:
            print("用户名或密码错误，若连续3次错误则自动锁死账号")
            count += 1
    if count>3:
        x = false