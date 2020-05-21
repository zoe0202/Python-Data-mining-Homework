count = 0

class Media(object):
    def __init__(self,name,url):
        self._name = name
        self._url = url
        global count
        count += 1
    def infor(self):
        print("名称为：",self._name)
        print("网址为：",self._url)
    def __str__(self):
        print("名称为：",self._name)

web = {"baidu":"https://www.baidu.com/","wix":"https://www.wix.com/"}
for i in web:
    media = Media(i,web[i])
    media.infor()
    media.__str__()
print("共实例化%d个媒体"%count)