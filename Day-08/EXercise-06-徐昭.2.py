"""使用正则表达式提取字符串中的邮箱
作者：徐昭"""


import re
def match_email():
    text = "scgthrxcegts@163.comxsafffff;3208413453@qq.comfff"
    m = re.findall(r'[0-9a-zA-Z_]{0,19}@[0-9a-z]{2,3}.com',text)
    if m:
        print(m)
    else:
        print("None")

match_email()



