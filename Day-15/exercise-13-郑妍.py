import requests
a = requests.get('http://whois.pconline.com.cn/ipJson.jsp')

r = requests.get('https://movie.douban.com/subject/1292052/')
print(r.url)
print(r.encoding == 'utf-8')
print(r.text)
print(r.content)
print(r.headers)
print(r.status_code)

#并不清楚作业是不是真的是这个意思……orz
