import re

#1. 使用正则表达式提取字符串中包含的所有手机号码
nums = 'my number is :13097347866'
numbers = re.split(':',nums)
print(numbers[1])

#2. 使用正则表达式判断字符串是否为邮箱地址
tail = input('Please write your letters: ')
if re.search('@',tail):
    print("It's an email")
else:
    print("I suppose it's not.")

#3. 使用正则表达式提取网页源代码中的所有Url
url_first = input('Please copy your source code there: ')
url_second = re.search(r'http://(.*)/',url_first,re.M|re.I|re.S)
out = url_second.group()
print(out)