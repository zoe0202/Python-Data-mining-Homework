import re

if __name__=='__main__':
    text=input('请输入：')
    email=re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+',text,re.M|re.I)
    if email:
        print('是邮箱')
    else:
        print('不是邮箱')



