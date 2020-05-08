#返回文件后缀名
import os.path 
def file_extension(path): 
  return os.path.splitext(path)[1] 
print file_extension('文件地址：')

#逗号分隔列表元素
list=['列表:']
for i in list:
 print(i,end=',')
