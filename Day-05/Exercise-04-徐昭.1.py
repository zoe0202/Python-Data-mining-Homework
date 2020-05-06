filename = input('请输入您的文件名: ')
#最后一次出现“.”的位置即是文件后缀名的位置
position = filename.rfind('.')

'''如果找不到，返回1，说明用户输入的格式有误，如果不是1的话，
就将position及以后的输出，即所谓的文件后缀名.'''

if position != -1:
    print ('您的文件后缀名为%s'%filename[position:])
else:
    print('您输入的文件名有误，请检查是否为全名！')
