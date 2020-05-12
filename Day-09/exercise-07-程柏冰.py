#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:cbb
import json

str = ""
with open('C:\\Users\\cbb\\Desktop\\聆听丶芒果鱼直播间时间切片弹幕.json',encoding='utf8')as f:
    data = f.read()
    jsonFile = json.loads(data)
    for i in jsonFile["data"]:
        if i[0] == "NM":
            str += ("\n" + i[3])
    file = open('result.txt', 'w', encoding='utf-8')
    file.write(str)
    file.close()
    print(jsonFile)