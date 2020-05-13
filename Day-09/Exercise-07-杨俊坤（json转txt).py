'''
将当前文件夹下的“聆听丶芒果鱼直播间时间切片弹幕.json”转存为txt格式，转存要求如下： 将弹幕类型为(列表中的第1项)为“NM”的弹幕的弹幕内容(列表中的第4项)取出，存为一条弹幕一行的txt格式。
'''


import json
def danmu():                                              #先定义了一个提取弹幕的函数
    try:
        list=[]                                                      #提前设置一个储存弹幕的列表
        with open(r'D:\Pyhton\Python-Data-mining-Tutorial\Week-02\聆听丶芒果鱼直播间时间切片弹幕.json','r',encoding='utf-8') as f:            #open函数读取文件
          file=json.load(f)                                   #运用load函数将json转为load函数      （貌似load生成的是个字典
          data = file['data']                               #用【'data'】是提取文件内'data'后的内容
        for i in data:                                       #循环提取
            if i[0]=="NM":                                #限制条件 让NM弹幕加入列表list  列表list就更新完毕
                list.append(i)                               #这里好像也可以直接加入i[3]
        y=open(r'C:\Users\NealPayne\Desktop\弹幕.txt','w',encoding='utf-8')      #读取文件
        for x in list:
            y.write(x[3]+'\n')          #写入文件
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('操作完成！')

if __name__ == '__main__':
    danmu()               #调用函数