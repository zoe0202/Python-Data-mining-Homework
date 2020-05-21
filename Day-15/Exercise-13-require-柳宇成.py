import requests

api_url = "http://whois.pconline.com.cn/ipJson.jsp"
r = requests.get(api_url)
print(r.status_code)
print(r.text)
