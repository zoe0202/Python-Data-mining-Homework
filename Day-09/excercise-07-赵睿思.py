import json
str = ""
with open('萝莉酱直播间时间切片弹幕.json', 'r') as f:#根据自己存放这个json的位置再改一下路径
    data = f.read()
    json_data = json.loads(data)
    for i in json_data["data"]:
        if i[0] == "NM":
            str += "\n" + i[3]
    fo = open("result.txt", "w")
    fo.write(str)
    fo.close()
    print('操作完成!')

if __name__ == '__main__':
    main()