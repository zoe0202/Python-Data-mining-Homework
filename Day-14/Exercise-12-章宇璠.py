class Media():
    count = 0

    def __init__(self, name, url):
        self.name = name
        self.url = url
        Media.count += 1

    def result(self):
        print('名称：', self.name)
        print('网址：', self.url)

    def str(self):
        print('媒体名：', self.name)

def main():
    media = {"百度": "www.baidu.com", "谷歌": "www.google.com", "b站": "www.bilibili.com"}
    for key in media.keys():
        m = Media(key, media[key])
        m.result()
        m.str()
    print('共实例化了%s个媒体' % Media.count)
if __name__ == '__main__':
    main()

