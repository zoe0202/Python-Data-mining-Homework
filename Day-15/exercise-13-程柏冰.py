# -*- coding:utf-8 -*-
import requests

#调用返回自己IP信息的API
URL = 'http://whois.pconline.com.cn/ipJson.jsp'
try:
    r = requests.get(URL)
    r.raise_for_status()
except requests.RequestException as e:
    print(e)
else:
    print(r.status_code)

#请求豆瓣电影中《肖申克的救赎》页面
url= 'https://movie.douban.com/subject/1292052/'
cookies= {'key':'value'}
headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
r = requests.post(url, headers=headers,cookies=cookies)
data=r.text
print (data)
