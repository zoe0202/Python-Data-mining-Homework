import re
text = "手机号码1为：13681177507，手机号码2为：13684698576"
num = re.split(r"\D",text)
for i in num:
    if len(i) == 11:
        print(i)
