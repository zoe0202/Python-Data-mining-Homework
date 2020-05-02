users = {'liu':123456,'wang':123456,'zhang':123456,'gong':123456,'jiang':123456}
def check_in(c):
    if c < 2:
        a = input('Name: ')
        b = input('Password: ')
        if b == users[a]:
            print('登陆成功')
        else:
            print('用户名或密码错误，若连续3次错误则自动锁死账号')
            c += 1
            check_in(c)
    else:
        a = input('Name: ')
        b = input('Password: ')
        if b == users[a]:
            print('登陆成功')
        else:
            print('因连续3次输入用户名或密码错误，账号已锁死')

check_in(0)