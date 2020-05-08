def fib(n):
    list = []

    def test(n):
        if n == 1 or n == 0:
            return 1
        else:
            return test(n - 1) + test(n - 2)

    for i in range(0, n + 1):
        list.append(test(i))
    return list[n - 1]


a = int(input('请输入数字：'))
print('第%d个斐波那契数为%d' % (a, fib(a)))
