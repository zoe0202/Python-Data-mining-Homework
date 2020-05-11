'''
-*- coding: utf-8 -*-
@Author  : liuyuxuan
正则表达式验证是否为电子邮箱名
'''
if __name__ == "_main_":
    import re

    string = input("please input your address:")
    string_re = "^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$"
    pattern = re.compile(string_re)
    result = pattern.match(string)

    if result == None:
        print("该邮箱名不合法")
    else:
        print("该邮箱名合法")


