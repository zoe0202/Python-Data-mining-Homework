"""
牛吃草问题
"""

def speed(w,x,y,z):
    Growth_Rate=(w*x-y*z)/(x-z)
    return Growth_Rate

def origina(s,t,u,v):
    Origina_amount=(s*t-u*v)
    return Origina_amount

def time(p,q,r):
    days=(p/(q+r))
    return days


a=int(input('第一种情况，青草供给的牛的头数a='))
b=int(input('可以吃的天数b='))
c=int(input('第二种情况，青草供给的牛的头数c='))
d=int(input('可以吃的天数d='))
g=int(input('如果供给的牛的头数g='))

i=speed(a,b,c,d)
j=origina(a,b,i,b)
k=time(j,g,i)
print('可以吃的天数是',k)