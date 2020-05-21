if __name__ == '__main__':
    import requests
    url = "https://movie.douban.com/subject/1292052/"
    header = {'user-agent': 'Evannafoxy/0.0.1'}  # 添加请求头部信息
    cookie = {'key': 'value'}
    r1 = requests.get(url, headers=header, cookies=cookie)
    r1.encoding = r1.apparent_encoding  # 避免因无法解析中文而产生乱码
    print(r1.status_code)  # 检查请求状态码
    print(r1.text)
