'''
-*- coding: utf-8 -*-
@Author  : liuyuxuan
转存JSON文件
'''
import json


def main():
    dict1 = {
        'username': input('please input your username:'),
        'password': input('please input your password:'),

        'info': [
            {'age': 19},
            {'job': 'studert'}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(dict1, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()
