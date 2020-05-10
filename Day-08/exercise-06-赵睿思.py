# 手机号提取
if __name__ == "__main__":
    import re
    tele_text = input('请输入包含手机号的文本：')
    telephone_number = re.findall(r"1\d{10}",tele_text)
    print(telephone_number)

# 判断是否为邮箱地址
if __name__ == "__main__":
    import re
    email = input('请输入您的地址：')
    pattern = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]'
    if re.match(pattern,email):
        print ("这是一个邮箱地址")
    else:
        print ("这不是一个邮箱地址")

#提取网页源代码中的url
if __name__ == "__main__":
    import re
    url_text = input('请输入你的网址：')
    url=re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',url_text)
    print(url)

#清理Twitter的Url
#清理Twitter的Url
if __name__ == "__main__":
    import re
    url_text = input('请输入你的网址：')
    url=re.findall('http?://www.twitter+.([^ ]*).com',url_text)
    print(url)