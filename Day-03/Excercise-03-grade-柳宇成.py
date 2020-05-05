grade = float(input("请输入成绩："))
if grade >= 90:
    level = "A"
elif grade >= 80:
    level = "B"
elif grade >= 70:
    level = "C"
elif grade >= 60:
    level = "D"
else:
    level = "E"
print("输入成绩对应的等级为：", level)
