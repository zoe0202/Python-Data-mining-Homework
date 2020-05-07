filename = input('请写入文件名')
list = filename.split('.')
print('后缀是'+str(list[-1]))
#好像写成print('',list[-1])更方便