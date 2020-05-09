#将计算有效互动比的方法写为函数并调用
def ratio(interaction, fans):
    yxhdb = interaction / fans
    return yxhdb
fans = int(input('粉丝量：'))
interaction = int(input('互动量：'))
print('有效互动比是：' + ratio)

#迭代实现菲波那切数列
def Fibonacci(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a
for i in Fibonacci(10):
    print(i)