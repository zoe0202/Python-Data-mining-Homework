import requests

r = requests.get('http://whois.pconline.com.cn/ipJson.jsp')

print(r.text)
