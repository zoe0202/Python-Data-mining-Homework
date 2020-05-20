'''
请求豆瓣电影中《肖申克的救赎》页面，并在控制台输出请求结果
'''
import requests
URL='https://movie.douban.com/subject/1292052/'
#定制头和cookie信息(其实我不知道为什么要这样做。。可是不这样做无法请求
data = {'some': 'data'}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}   #这个是再网页里扒的
cookie = {'key':'value'}
r=requests.get(URL,headers=header,cookies=cookie,data=data)

print('请求结果：',r.text)
if r.status_code==200:
    print('连接服务器成功')
else:
    print('连接服务异常')
if r.ok:  # 查看r.ok的布尔值便可以知道是否登陆成功
    print('登录成功')
else:
    print('登录失败')

