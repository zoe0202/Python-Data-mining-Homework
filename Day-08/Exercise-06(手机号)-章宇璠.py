if __name__ == "__main__":
    import re
    def get_findAll_mobiles(text):
        mobiles = re.findall(r"1\d{10}", text)
        return mobiles

    content = str(input("请输入一些数字："))
    moblies = get_findAll_mobiles(text=content)
    print(moblies)


