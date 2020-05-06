a=int(input("a="))
b=int(input("b="))
if a<=0 or b<=0:
    print('error')
else:
    while(b>0):
        temp=0
        temp=a%b
        a=b
        b=temp
    if a==1:
        print("互质")
    else:
        print("不互质")
