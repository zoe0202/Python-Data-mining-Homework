'''
-*- coding: utf-8 -*-
@Author  : liuyuxuan
正则表达式匹配手机号码
'''
if __name__ == "_main_":
    import re

    string = input("please input a string:")
    string_re = "1[3|5|7|8|]\d{9}"
    pattern = re.compile(string_re, )
    result = pattern.findall(string)
    print(result)

