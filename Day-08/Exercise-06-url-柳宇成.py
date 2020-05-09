import re

account = input('请输入网址：')

a = re.findall(r'twitter.com\w+', account)
print(a)
'''师哥，对这一个测试有点疑惑，希望您能在直播时讲解。还有想请问一下在处理pattern时有中文应该怎么办呀？'''