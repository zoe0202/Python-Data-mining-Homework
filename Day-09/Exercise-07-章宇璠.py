import json
def main():
    try:
        result = []
        with open('D:\\中国传媒大学\\大一下\\jupyter\\聆听丶芒果鱼直播间时间切片弹幕.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)
        for i in range(len(data['data'])):
            if data['data'][i][0] == 'NM':
                result.append(data['data'][i][3])
        a = open("D:\中国传媒大学\大一下\jupyter\out.txt", 'w+', encoding='UTF-8')
        for i in range(len(result)):
            print(result[i], file=a)
        a.close()
    except IOError as e:
        print(e)
    print('保存数据完成!')
if __name__ == '__main__':
    main()

