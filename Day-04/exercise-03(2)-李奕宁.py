a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a+b>c and a+c>b and b+c>a:
    l = a+b+c
    print("周长:",l)
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print("面积:",s)
else:
    print("不能构成三角形")
