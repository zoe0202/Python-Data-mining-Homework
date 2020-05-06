if __name__ == "__main__":
    def divide(a, b):
        c=b/a
        return c

a = float(input("请输入您的偶像的粉丝量："))
b = float(input("请输入您的偶像与粉丝的互动量："))
print("您的偶像与粉丝的有效互动比为：{}".format(divide(a,b)))




