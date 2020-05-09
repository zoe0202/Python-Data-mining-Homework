user = "徐昭"
password = "郭正一"
for i in range(3):
    username = input("请输入您的用户名：")
    Password = input("请输入您的密码：")
    if username == user and Password == password :
        print("欢迎%s ！" %user)
        break 
    else:
        print("用户名或密码错误！")
else:  
    print("您已经连续三次输入错误，账号已被冻结！")
