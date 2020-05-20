class media():
    count = 0

    def __init__(self, name, url):
        self.name = name
        self.url = url
        media.count += 1

    def output(self):
        print('名称：', self.name)
        print('网址：', self.url)

    def str(self):
        print('媒体名：', self.name)


web = {"百度": "www.baidu.com", "新浪": "www.sina.com", "网易": "www.163.com"}
for key in web.keys():
    w = media(key, web[key])
    w.output()
    w.str()
print('共实例化了%s个媒体' % media.count)
