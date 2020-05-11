"""使用正则表达式提取url
作者：徐昭"""

import re
import requests

def match_url():
    text = ""
    res = requests.get('http://www.cuc.edu.cn/')
    res.encoding = 'utf-8'
    url = re.findall(r'[a-zA-Z]+://[^\s]*[.com|.cn]', res.text)
    if url:
        print(url)
    else:
        print("None")
match_url()