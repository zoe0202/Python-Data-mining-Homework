import re
email = input("请输入邮箱地址：")
pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.+[a-zA-Z0-9_-]+$'
if re.match(pattern,email) == None:
    print('不是邮箱地址')
else:
    print("是邮箱地址")
