import re
email=input('请输入需要鉴别的文本')
pattern=r'\w+@\w+.\w+'
if re.match(pattern, email):
    print('这是一个有效的邮箱地址')
else:
    print('这不是一个有效的邮箱地址')