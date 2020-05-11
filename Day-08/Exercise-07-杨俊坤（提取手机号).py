'''
使用正则表达式提取字符串中包含的所有手机号码
'''
if __name__=='__main__':
    import re
    word =('15678988884hhbgmh15689785542ghfvhg18389883577ggjmb8952200')           #随便写了一个字符串
    pattern = re.compile(r'\d{11}')                                                                                  #用 re.compile编译正则表达式     r'\d{11}'取十一位数字
    phone_number=pattern.finditer(word)                                                                     #用finditer寻找符合条件的数字并用迭代返回
    for i in phone_number:                                                                                             #for in循环
      print(i.group())
