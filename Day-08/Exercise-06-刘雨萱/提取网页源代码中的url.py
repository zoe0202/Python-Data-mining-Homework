'''
-*- coding: utf-8 -*-
@Author  : liuyuxuan
提取网页源代码中的url
'''
if __name__ == "_main_":
    import re
    import requests

    url = input("please input your url:")
    response = requests.get(url)
    data = response.text
    pattern = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    result = pattern.findall(data)
    print(result)

