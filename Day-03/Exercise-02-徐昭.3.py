while True:
    Fans,HFans =input("请输入粉丝数和互动量，并以空格分开:\n").split()
    if (Fans.isdigit() and HFans.isdigit()):
        Fans=int(Fans)
        HFans=int(HFans)
        YX = HFans / Fans
        print("该明星的粉丝有效互动比为{:.2f}".format(YX))
        break
    else:
        print("您输入的数据有误，请输入正确的数据！")
        


 

