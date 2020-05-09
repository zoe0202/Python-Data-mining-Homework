def f(m=0,n=0):
    '''有效互动比'''
    x = float(m/n)
    return x
m = int(input("请输入粉丝量："))
n = int(input("请输入互动量："))
if __name__=="__main__":
    print("有效互动比为：%f" % f(m,n))