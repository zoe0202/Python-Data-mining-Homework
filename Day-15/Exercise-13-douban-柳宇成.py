import requests

douban_url = "https://movie.douban.com/subject/1292052/"
cookies = {'key': 'value'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
r = requests.post(douban_url, headers=headers, cookies=cookies)
print(r.text)
