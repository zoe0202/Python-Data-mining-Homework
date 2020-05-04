a=int(input("请输入整数1"))
b=int(input("请输入整数2"))
c=min(a,b)
i=2
for i in range(i,c+1):
    if a%i==0:
        if b%i==0:
            print("不互质")
            break
else:
    print("互质")
