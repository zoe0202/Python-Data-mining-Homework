import requests

ret = requests.get("http://whois.pconline.com.cn/ipJson.jsp")
print(ret.text)