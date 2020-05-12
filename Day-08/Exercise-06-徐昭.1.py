"""使用正则表达式提取字符串中的手机号
作者：徐昭"""

import re
def match_phone():
    text = "aaabbbcc13809148338eedfsfsf15702957315ksfss;13571708019fsdfk15114809485sfksfsf;sk;sfkskf;sfsk"
    #这里只是测试一下，修改成input 也可以
    m = re.findall(r"1[358]\d{9}", text)
    if m:
        print(m)
    else:
        print("None")

match_phone()