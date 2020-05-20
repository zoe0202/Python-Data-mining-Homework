'''
!/usr/bin/env python
-*- coding:utf-8 -*-
Author:liuyuxuan
访问网络资源
'''
import requests
# 请求调用API
API_url="http://whois.pconline.com.cn/ipJson.jsp"
r=requests.get(API_url)
print(r.status_code)#检查请求状态码
print(r.text)
#求豆瓣电影中《肖申克的救赎》页面
movie_url="https://movie.douban.com/subject/1292052/"
header = {'user-agent': 'my-app/0.0.1'}# 添加请求头部信息，解决反爬程序问题
cookie = {'key':'value'}
r1=requests.get(movie_url,headers=header,cookies=cookie)
r1.encoding =r1.apparent_encoding #避免因无法解析中文而产生乱码
print(r1.status_code)#检查请求状态码
print(r1.text)

