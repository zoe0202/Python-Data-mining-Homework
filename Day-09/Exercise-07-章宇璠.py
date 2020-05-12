if __name__ == '__main__':
    import json
    result = []
    with open('D:\\中国传媒大学\\大一下\\Python-Data-mining-Tutorial\\Week-02\\萝莉酱直播间时间切片弹幕.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
    for i in range(len(data['data'])):
        if data['data'][i][0] == 'NM':
            result.append(data['data'][i][3])
    a = open("D:\中国传媒大学\大一下\jupyter\out.txt", 'w+')
    for i in range(len(result)):
        print(result[i], file=a)
    a.close()