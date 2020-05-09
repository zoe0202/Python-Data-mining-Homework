import re

email = input('请输入邮箱：')
pattern = r'\w+@\w+.\w+'

if re.match(pattern, email):
    print('输入邮箱地址有效')
else:
    print('输入邮箱地址无效')
