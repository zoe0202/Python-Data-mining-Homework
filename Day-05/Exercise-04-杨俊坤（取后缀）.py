def suffix(filename):              #定义后缀名函数
    dot = filename.rfind('.')          #用rfind从右到左定位.的位置
    return filename[dot + 1:] if dot > 0 else ''    #用切片操作取出后缀名 （为什么用else不太明白,，但是去掉以后不太正确）
print(suffix(''))
