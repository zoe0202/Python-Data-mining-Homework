"""
目的：实现调用返回自己IP信息的API
作者：徐昭
"""

import requests
import re
import json

r = requests.get('http://whois.pconline.com.cn/ipJson.jsp')   #发送get请求

text = re.findall("{[^{}]+\}", r.text)[0] #提取网站返回的信息

data = json.loads(text)  #转换为python对象

for dict_key, dict_value in data.items():
    print(dict_key,': ',dict_value)   #把字典里的信息打印出来

