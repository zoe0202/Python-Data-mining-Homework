'''
用返回自己IP信息的API，其Url如下：http://whois.pconline.com.cn/ipJson.jsp
'''
import requests
def get_API():
    URL='http://whois.pconline.com.cn/ipJson.jsp'
    r=requests.get(URL)
    if r.ok:                 #查看r.ok的布尔值便可以知道是否登陆成功
        print('登录成功')
    else:
        print('登录失败')
    print('响应状态码:',r.status_code )       #响应状态码
    print('API是：',r.text)          #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码
get_API()

#看理论有点抽象，就把能试的试了一下