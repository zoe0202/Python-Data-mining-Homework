user_name = '123'
user_password = 'abc'
i = 3
while i > 0:
    user_name_input = input('请输入用户名：')
    user_password_input = input('请输入密码：')
    if user_name == user_name_input and user_password == user_password_input:
        print('登陆成功！')
        break
    else:
        print('用户名或密码错误，若连续3次错误则自动锁死账号！')
        if i == 1:
            print('因连续3次输入用户名或密码错误，账号已锁死！')
        i -= 1
