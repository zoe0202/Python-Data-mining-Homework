#author:zhouyueting
#name:转存Json数据
import json
import os
json_data = open("聆听丶芒果鱼直播间时间切片弹幕.json","rb")#打开json文件，注意后面是“rb”
info_data = json.load(json_data)#将json格式数据转化为python可操作的字典，不知道问什么json.loads不行
list_data = info_data["data"]#将字典中的key data提取出来，成为列表
new_data = []
final_data = []
def is_data(list):#定义一个判定列表第一个元素是否为“NM”的函数
    if list[0] == "NM":
        return True
    else:
        return False
pos = (n for n in list_data if is_data(list=n))#构造一个生成器，用于筛选原始data列表中的元素
for x in pos:
    data = x
    new_data.append(x)#将符合条件的元素加入new_data列表
for i in new_data:
    element = i[3]
    final_data.append(element)#将元素（列表）中的第三项元素提出来，形成新的列表
final_data_str = ("\n".join(final_data))#将最终的列表转化为字符串，并转行
path = os.getcwd()#获取当前执行文件的路径
if os.path.exists("data.txt"):
    f = open("data.txt", "w+",encoding='utf-8')
else:
    if os.path.isdir(path) :
        f = open("data.txt","w+")#在当前路径创建并打开一个txt文件
f.write(final_data_str)#写进去，啊啊啊啊啊，大功告成！！！头也秃了TT
f.seek(0)
f.close()
