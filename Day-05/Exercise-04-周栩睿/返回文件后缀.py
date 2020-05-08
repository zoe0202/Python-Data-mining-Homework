filename = input("输入文件名")


def get_suffix(filename, has_dot=False):
    str = "filename"
    str = "."
    pos = str.rfind(str)
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return '不符合要求'


print(get_suffix(filename, has_dot=False))
