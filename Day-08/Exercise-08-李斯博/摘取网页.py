import re
a=input('请输入想要摘取的网页代码')
b=re.findall(r'www.\w+.\w{2,3},a')
print(b)