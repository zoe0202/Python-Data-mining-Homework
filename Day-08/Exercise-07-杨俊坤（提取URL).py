'''
使用正则表达式提取网页源代码中的所有Url
'''
import re
if __name__=='__main__':
  word=str(input('请输入包含URL的字符串:'))
  URL=re.finditer('[a-z]+?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', word,re.I)                     #写出正则式 貌似找多个只能用finditer （search不行） 下次可以用strip试试
  for i in URL:
    print(i.group())                                                                                                   #用group分组提取出内容 一个小注意点是有了i就不能写i.URL了，不然程序会报错