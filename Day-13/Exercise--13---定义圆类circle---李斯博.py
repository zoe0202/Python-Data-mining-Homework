class Circle:
    def __init__(self, radius):#设置radius为圆的半径

        self.radius = radius

    def perimeter(self): #计算圆的周长的公式
        girth = 3.14 * 2 * self.radius
        return (girth)

    def area(self):#计算圆面积长的公式
        acreage = 3.14 * self.radius * self.radius
        return (acreage)


def main(): #程序运行过程
    radius = float(input("请输入需要求得的圆的半径:"))
    f = Circle(radius)
    print('所求的圆的面积为：%.2f' % float(f.area()))
    print('所求的圆的周长为：%.2f' % float(f.perimeter()))


if __name__ == '__main__':
    main()