import requests
import json
r = requests.get('http://whois.pconline.com.cn/ipJson.jsp')
r.encoding = 'GBK'
print(r.text)

#r1= requests.get('https://movie.douban.com/subject/1292052/')
r1 = requests.head(url='https://movie.douban.com/subject/1292052/', params={'wd': 'python'}) # 带参数的get请求
#r1 = requests.get('https://movie.douban.com/subject/1292052/')
r1.encoding = 'utf-8'
print(r1.text)
print(r1.encoding)
print(r1.status_code)
print(r1.content)
print(r1.headers)

