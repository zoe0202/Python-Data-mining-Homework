import json
import re
#读取弹幕文件导入python
with open(r"C:\Users\admin\Documents\GitHub\Python-Data-mining-Tutorial\Week-02\聆听丶芒果鱼直播间时间切片弹幕.json", encoding='utf-8') as f:
    data = json.loads(f.read())
    list1 = data['data']
    list2 = []
    for i in list1:
        if i[0] == "NM":
            c = i[3]
            list2.append(c)
            correctline = str('\n'.join(list2))
    print(correctline)
with open("弹幕.txt", "w") as f:
        f.write(correctline)


