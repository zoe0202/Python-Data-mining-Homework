import time
import datetime
time.sleep(1)
t = datetime.datetime.now()
strt = t.strftime("%Y-%m-%d %H:%M:%S")
print(strt,type(strt))