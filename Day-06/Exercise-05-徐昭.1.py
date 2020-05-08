def youxiao(Fans,HFans):
    YX = HFans/Fans
    return YX


if __name__ == '__main__':
    Fans,HFans =map(int,input("请输入粉丝数和互动量，并以空格分开:\n").split())
    
    print("该明星的粉丝有效互动比为{:.2f}".format(youxiao(Fans,HFans)))
