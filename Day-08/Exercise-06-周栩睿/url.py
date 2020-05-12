import re
def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url
string = '百度的网页地址为：https://www.baidu.com，bilibili的网页地址为：https://space.bilibili.com'
print("Urls: ", Find(string))