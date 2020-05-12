import re

if __name__=='__main__':
    text=input('请输入：')
    urls = re.findall(
        r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)",
        text)
    urls = list(sum(urls, ()))
    urls = [x for x in urls if x != '']
    print(urls)
