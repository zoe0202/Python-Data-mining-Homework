import json

with open("聆听丶芒果鱼直播间时间切片弹幕.json", "r", encoding='utf-8') as a:
    data = json.loads(a.read())
    list1 = data['data']
    list2 = []
    for i in list1:
        if i[0] == "NM":
            c = i[3]
            list2.append(c)
            str1 = str('\n'.join(list2))
    print(str1)
    with open("exercise-07-郑妍.txt", 'w',encoding='utf-8') as b:
        b.write(str1)
