import json

if __name__ == '__main__':
    str = ''

with open('聆听丶芒果鱼直播间时间切片弹幕.json', 'r', encoding='UTF-8')as f:#需更改文件路径
    dict = json.load(f)
    for n in dict['data']:
        if n[0] == 'NM':
            str += n[3] + '\n'
print(str)#检测是否读写成功

file = open('b.txt', 'w', encoding='UTF-8')#需更改文件路径
file.write(str)
file.close()
