''''''
'百分制成绩转换成等级制成绩'
'Author：李斯博'
''''''

score = float(input('请输入成绩：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是', grade)
