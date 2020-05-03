a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a<=0 or b<=0 or c<=0:
    print("Error")
elif a+b>c and a+c>b and b+c>a:
    print("T")
else:
    print("F")
