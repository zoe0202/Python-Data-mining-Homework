count=1
while count<=3:
    user_name=input('请输入你的账号：')
    password = int(input('请输入你的密码：'))
    count=count+1
    if user_name == 'lisibo' and password =='123456':
       print('登陆成功')
       break
    elif count == 4:
        print('失败三次，机会为0')
    elif user_name == 'false' and password =='false':
        print('用户密码不能为空')
    else:
        print('用户名或密码错误，请重试')