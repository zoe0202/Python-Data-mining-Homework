import math

r=float(input("r="))
if r<0:
    print("error")
else:
    c=math.pi*2*r
    s=math.pi*math.pi*r
    print("c=",c)
    print("s=",s)
