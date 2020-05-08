a=1
b=1
from time import sleep
while True:
    print(min(a,b))
    if min(a,b)==a:
        a=a+b
        sleep(1)
    else:
        b=a+b
        sleep(1)
