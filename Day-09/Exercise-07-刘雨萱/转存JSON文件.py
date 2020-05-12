'''
-*- coding: utf-8 -*-
@Author  : liuyuxuan
转存JSON文件
'''

import json


def main():
    with open('聆听丶芒果鱼直播间时间切片弹幕.json')as f:
        f_json = json.reader(f)
        for row in f_json:
            if row[1] == 'NM':
                try:
                    with open("test.json", "w", encoding='utf-8') as f1:
                        data = json.loads(f.read(row[4]), '/n')
                except IOError as e:
                    print(e)
                print('保存数据完成!')


if __name__ == '__main__':
    main()
