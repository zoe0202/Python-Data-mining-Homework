'''
使用正则表达式判断字符串是否为邮箱地址
'''
if __name__=='__main__':
    import re
    email = str(input('请输入你的邮箱地址：'))
    address=re.search(r'\w+@\w+\.[a-z]+',email,re.I)                                             #用re.search定义了字符串的格式
    if address.group()==email:                                                                            #这里应该有两种方法，第一种是用group()提取内容然后如果符合输入值的话就正确
        print('邮箱地址正确')                                                                                      #第二种就是直接写if address= 可以这样子判断是因为search(或match)函数返回的是布尔值，本身就有判断的意味
    else:
        print('邮箱地址错误')