a=input("输入你的邮箱地址：")
import re
def judge_email(a):
    b=re.match("((.*)@(.*).[(cn)|(com)|(gov)])",a)
    return b
if judge_email(a):
    print("这是一个邮箱地址")
else:
    print("这不是一个邮箱地址")
