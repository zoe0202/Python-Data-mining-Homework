'''
百分制成绩转换为等级制成绩
'''
score = int(input("请输入您的百分制成绩："))#用户键入百分制成绩
if score < 60:#判断成绩等级并输出
    print("您的成绩等级为：不合格")
elif score >= 60 and score < 80:
    print("您的成绩等级为：合格")
elif score >= 80 and score < 90:
    print("您的成绩等级为：良好")
else:
    print("您的等级为：优秀")