
a=set()
def g(x):
    if x==1:
        a.add(1)
        return 1
    elif x==2:
        a.add(1)
        a.add(2)
        return 2
    b=g(x-1)+g(x-2)
    a.add(b)
    return b
num=int(input('输入打印斐波那契数列的个数：'))
b=g(num)
L=list(a)
L.sort()
print(L)
