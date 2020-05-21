import requests

url = "https://movie.douban.com/subject/1292052/"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

ret = requests.get(url,headers = header)#添加头部信息，针对反爬虫
print(ret.status_code)#输出状态码，看是否为200
print(ret.text)