import requests
#调用返回自己IP信息的API
r = requests.get('http://whois.pconline.com.cn/ipJson.jsp')
print(r.text)
r.raise_for_status()#如果不是200，抛出异常
#请求豆瓣电影中《肖申克的救赎》页面
r = requests.post('https://movie.douban.com/subject/1292052/')
print(r.text)
#创建头部
header = {'user-agent': 'my-app/0.0.1'}
cookie = {'key':'value'}
r1 = requests.get('https://movie.douban.com/subject/1292052/',headers=header,cookies=cookie)
print(r1.text)
r.raise_for_status()#如果不是200，抛出异常