score=float(input('请输入你的成绩：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:grade = 'E'
print('你成绩的等级为：',grade)
