if __name__ == '__main__':
    import requests
    payload = {'key1': 'value1', 'key2': 'value2'}
    ret = requests.get("http://whois.pconline.com.cn/ipJson.jsp", params=payload)
    print(ret.status_code)  # 检查请求状态码
    print(ret.text)