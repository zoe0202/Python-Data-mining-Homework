import json
import re


def main():
    with open(r'C:\Users\Surface\Desktop\聆听丶芒果鱼直播间时间切片弹幕.json', 'r', encoding='utf-8') as f:
        context = json.load(f)
    result = \
        [
            str(x[3]) + "\n" for x in context["data"]
            if (x[0] == "NM")
        ]

    with open('result.txt', 'w', encoding='utf-8') as fs:
        fs.writelines(result)
    return


if __name__ == '__main__':
    main()
