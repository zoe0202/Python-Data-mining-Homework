import re

add = input('请输入网页源代码：')

a = re.findall(r'www.\w+.\w{2,3}', add)
print(a)
