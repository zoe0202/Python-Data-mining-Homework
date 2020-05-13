"""
目的：按照要求提取弹幕
作者：徐昭
"""


import json

json_path = 'E:\\Python\\danmu.json'
gai = []  # 将修改过后的弹幕数据存储到这里
with open(json_path, 'r', encoding='utf-8', errors='ignore') as f: #我只需要读取json文件就好了
    danmu = json.load(f) #读取弹幕文件中的弹幕
    data = danmu["data"]
    for i in data:
        if i[0] == "NM":
            gai.append(i[3])

filename = 'E:\\Python\\gaixie.txt'
with open(filename, 'w', errors='ignore') as f2: #只需要可写
    for i in gai:
        f2.write(i)
        f2.write("\n") #一行存储一条弹幕




