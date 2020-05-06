grade = float(input('请告诉我你的成绩'))
if grade >= 90:
    achievement = 'A'
elif grade >= 80:
    achievement = 'B'
elif grade >= 70:
    achievement = 'C'
elif grade >= 60:
    achievement = 'D'
else:
    achievement = 'E'
print('你的等级制成绩是：'+str(achievement))