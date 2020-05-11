import re

if __name__=='__main__':
    text=input('请输入：')
    mobile = re.findall(r"1\d{10}", text)
    print (mobile)