'''调用返回自己IP信息的API'''
import requests
r = requests.get('http://whois.pconline.com.cn/ipJson.jsp')
# print(r.status_code)
# print(r.url)
print(r.text)
'''请求网页'''
from bs4 import BeautifulSoup
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
response = requests.get(url="https://movie.douban.com/subject/1292052/",headers=headers)
print(response.status_code)
# print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
tags = soup.find_all(type="application/ld+json")
print(tags)