def count(inter, supp):
    inter = input("请输入您的互动量：")
    supp = input("请输入您的粉丝量：")
    inter = float(inter)
    supp = float(supp)
    E = inter / supp
    return E
    print("您的有效互动比为{:.2f}".format(E))


if __name__ == '__count__':
    count()
