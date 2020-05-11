import re
def jud_email(email):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
    if re.match(pattern,email)!= None:
        print("输入的邮箱地址格式正确！")
    else:
        print("输入的邮箱地址错误!")
input_email = input("请输入邮箱地址:")
print(jud_email(input_email))