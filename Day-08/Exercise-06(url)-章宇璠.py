if __name__ == "__main__":
    import re
    def Find(string):
        url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
        return url
    string = str(input("请输入网页源代码："))
    print("Urls: ", Find(string))