"""
目的：抓取“肖申克的救赎”的相关休息
作者：徐昭
"""

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
url = 'https://movie.douban.com/top250?start=0&filter='

proxies = {
    "http": "http://123.207.96.189:80"
}

url = 'https://movie.douban.com/subject/1292052/'  # 爬取的网址

response = requests.get(url, proxies = proxies,headers=headers)  #获取信息
text = response.text   # 解码
print(text)