import xlwt
import json
with open("萝莉酱直播间时间切片弹幕.json", "r", encoding='utf-8') as a:
    data = json.loads(a.read())
    list1 = data['data']
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'类别')
worksheet.write(0,1,'发布时间')
worksheet.write(0,2,'发布者')
worksheet.write(0,3,'弹幕内容')
worksheet.write(0,4,'弹幕包含颜文字')
for i in range(0,len(list1)):
    for j in range(5):
        worksheet.write(i+1,j,list1[i][j])
workbook.save('exercise-10-郑妍.xls')
