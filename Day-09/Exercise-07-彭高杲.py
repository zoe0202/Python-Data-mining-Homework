#读写文件好难我没有了我不会我不会我不会我不会我不会我不会
#bug永无止境调bug使人快乐使人飘飘欲仙awsl
#在调了一下午+一晚上各种类型的鬼畜bug后我写了以下两种

import json
#第一种方法有点啰嗦
#读入文件并判断
def interpret_data():
    with open(r"E:\大学\项目\华榜\培训\Python-Data-mining-Tutorial\Week-02\萝莉酱直播间时间切片弹幕.json", "rb") as file:
        content = json.load(file)["data"]
    return [x[3] for x in content if (x[0] == "NM")]
#我应该怎样才能在txt中输出这段东西
fw = open("E:\大学\项目\华榜\培训\Exercise\SoHard.txt", "w")
out = [str(i) for i in interpret_data()]
for line in out:
    fw.write(line.encode("gbk", 'ignore').decode("gbk", "ignore")+"\n")
fw.close()

#第二种方法海星
def interpretData():
    with open(r"E:\大学\项目\华榜\培训\Python-Data-mining-Tutorial\Week-02\萝莉酱直播间时间切片弹幕.json", "rb") as file:
        content = json.load(file)
    result = [str(x[3]) + "\n" for x in content["data"] if (x[0] == "NM")]
    with open(r"E:\大学\项目\华榜\培训\Exercise\ExcuseMe.txt", "w") as file:
        file.writelines(result)
    return
interpretData()