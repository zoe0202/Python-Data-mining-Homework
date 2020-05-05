a=int(input("请输入一大于1的整数"))
for i in range (2,a//2+1):
    if a%i==0:
        print("不是质数")
        break
else:
    print("是质数")
