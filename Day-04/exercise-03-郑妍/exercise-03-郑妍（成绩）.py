a=int(input("请输入成绩"))
if 0<=a<60:
    print("不合格")
elif a<75:
    print("合格")
elif a<85:
    print("良好")
    break
elif a<=100:
    print("优秀")
else:
    print("成绩输入错误")
