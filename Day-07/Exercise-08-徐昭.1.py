import time
import datetime
time1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("现在时间：",time1)
time.sleep(1)
time2=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print("暂停一秒：",time2)
