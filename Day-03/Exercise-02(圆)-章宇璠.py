if __name__ == "__main__":
    import math
    r = input("请输入您的圆的半径：")
    r = float(r)
    pi = math.pi
    c = 2 * pi * r
    s = r ** 2 * pi
    print("该圆的周长为{:}，该圆的面积为{:}".format(c, s))
