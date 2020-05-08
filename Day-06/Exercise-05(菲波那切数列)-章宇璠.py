if __name__ == "__main__":
    s = set()
    def g(x):
        if x == 1:
            s.add(1)
            return 1
        elif x == 2:
            s.add(1)
            s.add(2)
            return 2
        ret = g(x - 1) + g(x - 2)
        s.add(ret)
        return ret
    num = int(input('请输入想要打印的斐波那契数列的个数：'))
    ret = g(num)
    L = list(s)
    L.sort()
    print(L)

