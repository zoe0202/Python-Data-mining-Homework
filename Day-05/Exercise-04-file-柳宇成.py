import os.path


def file_extension(path):
    return os.path.splitext(path)[1]


file = input('请输入文件名：')
print('文件的格式为：%s' % file_extension(file))

