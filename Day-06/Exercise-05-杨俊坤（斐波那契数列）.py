def 斐波那契数列(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
        yield a
for i in 斐波那契数列(20):      #括号内的数字即输出前N项
    print(i, end=' ')
